import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')

    # Get all snapshots owned by me
    response = client.describe_snapshots(OwnerIds=['self'])

    # Get all active Instance IDs
    instances = client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = {}

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Interact with each snapshot and delete if it is not associated with any active instance
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            # Delete snapshot if it is not associated with any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted snapshot {snapshot_id} as it is not associated with any volume")

        else:
            # Check if the volume still exists
            try:
                volume_response = client.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted snapshot {snapshot_id} as it was taken from a volume not attached to any instance")

            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted snapshot {snapshot_id} as the volume associated with it no longer exists")