"""
BotoEc2 Class for working with AWS EC2 instances.
v. 0.1
"""
import boto3
from botocore.exceptions import ClientError


class BotoEc2():
    def __init__(self):
        """ Class for working with AWS EC2 instances. """
        self.ec2_resource = boto3.resource('ec2')
        self.ec2_client = boto3.client('ec2')

    def create_instance(self, arg_image_id='ami-0d16ecbd2762ae54a', arg_subnet_id='subnet-0249a968'):
        """ Create new EC2 Instance """
        try:
            print('Lets create new instance.')
            instance = self.ec2_resource.create_instances(ImageId=arg_image_id, MaxCount=1, MinCount=1,
                                                          InstanceType='t2.micro', SubnetId=arg_subnet_id)
            instance[0].wait_until_exists()
            return [True, instance]
        except ClientError as err:
            return [False, self.parse_exception('create_instance', err)]

    def start_instance(self, arg_instance_id):
        """ Run EC2 instance by ID """
        try:
            print(f'Run Instance "{arg_instance_id}".')
            instance = self.ec2_resource.Instance(arg_instance_id)
            instance.start()
            instance.wait_until_running()
            print(f'Instance "{instance.id}" has started.')
            return [True, '']
        except ClientError as err:
            return [False, self.parse_exception('start_instance', err)]

    def stop_instance(self, arg_instance_id):
        """ Stop EC2 instance by ID """
        try:
            print(f'Instance "{arg_instance_id}" stopping begins.')
            instance = self.ec2_resource.Instance(arg_instance_id)
            instance.stop()
            instance.wait_until_stopped()
            print(f'Instance "{instance.id}" has stopped.')
            return [True, '']
        except ClientError as err:
            return [False, self.parse_exception('stop_instance', err)]

    def reboot_instance(self, arg_instance_id):
        """ Reboot EC2 instance by ID """
        try:
            print(f'Instance "{arg_instance_id}" rebooting begins.')
            instance = self.ec2_resource.Instance(arg_instance_id)
            instance.stop()
            instance.wait_until_stopped()
            print(f'Instance "{instance.id}" has stopped.')

            instance.start()
            instance.wait_until_running()
            print(f'Instance "{instance.id}" has started.')

            return [True, '']
        except ClientError as err:
            return [False, self.parse_exception('reboot_instance', err)]

    def remove_instance(self, arg_instance_id):
        """ Remove EC2 instance by ID """
        try:
            print(f'Instance "{arg_instance_id}" removing begins.')
            instance = self.ec2_resource.Instance(arg_instance_id)
            instance.terminate()
            instance.wait_until_terminated()
            return [True, '']
        except ClientError as err:
            return [False, self.parse_exception('remove_instance', err)]

    def terminate_all(self):
        """ Terminate all available instances. """
        try:
            print(f'Terminate all instances in list: {self.get_instances()[1]}')
            # self.ec2_resource.instances.terminate()
            return [True, '']
        except ClientError as err:
            return [False, self.parse_exception('terminate_all', err)]

    def get_instances(self, arg_region=None, arg_status=None):
        """
        Return EC2 instances list or None.
        :param arg_region: Region for filtering. Default: None
        :type arg_region: str
        :param arg_status: Instance status [running, stopped, terminated, ...]. Default: None
        :type arg_status: str

        :return: a list of the instances or empty list if there are no instances
        :rtype: list
        """
        try:

            # Init instances empty filter
            instances_filter = []

            if arg_region is not None:
                instances_filter.append({'Name': 'availability-zone', 'Values': [arg_region]})

            if arg_status is not None:
                if arg_status == 'started':
                    arg_status = 'running'
                instances_filter.append({'Name': 'instance-state-name', 'Values': [arg_status]})

            # Get instancesCollectionManager
            instances = self.ec2_resource.instances.filter(Filters=instances_filter)

            instances_lst = [inst.id for inst in instances]

            return [True, instances_lst]
        except ClientError as err:
            return [False, self.parse_exception('get_instances', err)]

    @staticmethod
    def parse_exception(arg_action, arg_exception):
        """ Simple parsing of AWS Client Error exception. Print type of error and return information about error. """
        # print(arg_exception)
        if arg_exception.response['Error']['Code'] == 'InvalidSubnetID.NotFound':
            print(f'BotoEc2() Error: "SubnetID Not Found". '
                  f'\n\t Class Method: {arg_action}, \n\t aws operation: {arg_exception.operation_name} \n\t '
                  f"Message: {arg_exception.response['Error']['Message']}")
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        if arg_exception.response['Error']['Code'] == 'InvalidAMIID.Malformed':
            print(f'BotoEc2() Error: "Invalid AMI ID". '
                  f'\n\t Class Method: {arg_action}, \n\t aws operation: {arg_exception.operation_name} \n\t '
                  f"Message: {arg_exception.response['Error']['Message']}")
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        if arg_exception.response['Error']['Code'] == 'InvalidParameterValue':
            print(f'BotoEc2() Error: "Invalid Parameter Value". '
                  f'\n\t Class Method: {arg_action}, \n\t aws operation: {arg_exception.operation_name} \n\t '
                  f"Message: {arg_exception.response['Error']['Message']}")
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        if arg_exception.response['Error']['Code'] == 'InvalidInstanceID.Malformed':
            print(f'BotoEc2() Error: "Invalid Instance ID". '
                  f'\n\t Class Method: {arg_action}, \n\t aws operation: {arg_exception.operation_name} \n\t '
                  f"Message: {arg_exception.response['Error']['Message']}")
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]

        else:
            print(f'BotoEc2() Error: "Other Exception. Please parse the response.". '
                  f'\n\t Class Method: {arg_action}, \n\t aws operation: {arg_exception.operation_name} \n\t '
                  f"Message: {arg_exception.response['Error']['Message']}")
            print(arg_exception.response)
            return [{arg_exception.operation_name}, arg_exception.response['Error']['Code'],
                    arg_exception.response['Error']['Message'], arg_exception.response]


if __name__ == "__main__":
    cls_ec2 = BotoEc2()
    # print(cls_ec2.create_instance(arg_image_id='ami-0d16ecbd2762ae54a', arg_subnet_id='subnet-0249a968'))
    # inst_cr_response = cls_ec2.create_instance(arg_image_id='ami-0d16ecbd2762ae54a', arg_subnet_id='subnet-0249a968')
    # instance = inst_cr_response[1]
    # print(inst_cr_response[0])
    # print(instance[0].id)

    # cls_ec2.start_instance('i-0515e9d361c16f4af')
    # cls_ec2.stop_instance('i-0bfb195bd59e70a44')
    # cls_ec2.reboot_instance('i-0515e9d361c16f4af')

    # print('Running instances: ', cls_ec2.get_instances(arg_region='eu-central-1a', arg_status='running'))
    # print('Running instances: ', cls_ec2.get_instances(arg_region='eu-central-1a', arg_status='started'))
    # print('Stopped instances: ', cls_ec2.get_instances(arg_region='eu-central-1a', arg_status='stopped'))
    # print('Terminated instances: ', cls_ec2.get_instances(arg_region='eu-central-1a', arg_status='terminated'))
    # cls_ec2.terminate_all()

    # print(cls_ec2.remove_instance('i-08efdbebd85370af5'))

    # "eu-central-1", "stopped", "start"
    # "eu-central-1", "started", "reboot"
    for inst in cls_ec2.get_instances(arg_region='eu-central-1a', arg_status='stopped')[1]:
        cls_ec2.start_instance(inst)

    for inst in cls_ec2.get_instances(arg_region='eu-central-1a', arg_status='started')[1]:
        cls_ec2.reboot_instance(inst)
