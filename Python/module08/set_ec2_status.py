""" Module 08. Exercise 2
"eu-central-1", "stopped", "start"
"eu-central-1", "started", "reboot"
"""

import argparse
from aws.boto_ec2 import BotoEc2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="'#### Change status of EC2 instances. ####'")
    parser.add_argument('region', metavar='REGION', help='Region: "eu-central-1".')
    parser.add_argument('status', metavar='STATUS',
                        help='Status: [stopped | started].', choices=['stopped', 'started'])
    parser.add_argument('action', metavar='ACTION',
                        help='Action: [start | reboot].', choices=['start', 'stop', 'reboot'])
    args = parser.parse_args()
    # print(args)

    cls_ec2 = BotoEc2()

    if args.status == 'stopped':
        if args.action == 'start':
            instances = cls_ec2.get_instances(arg_region=args.region, arg_status=args.status)[1]
            if not instances:
                print('There are no instances starting.')
                raise SystemExit(1)
            for inst in instances:
                cls_ec2.start_instance(inst)
        elif args.action == 'reboot':
            print('Reboot action for stopped instances is not available.')
        elif args.action == 'stop':
            print('Stop action for stopped instances is not available.')
    else:
        if args.action == 'reboot':
            instances = cls_ec2.get_instances(arg_region=args.region, arg_status=args.status)[1]
            if not instances:
                print('There are no instances for rebooting.')
                raise SystemExit(1)
            for inst in instances:
                cls_ec2.reboot_instance(inst)
        elif args.action == 'stop':
            instances = cls_ec2.get_instances(arg_region=args.region, arg_status=args.status)[1]
            if not instances:
                print('There are no instances for stopping.')
                raise SystemExit(1)
            for inst in instances:
                cls_ec2.stop_instance(inst)

        elif args.action == 'start':
            print('Start action for running instances is not available.')
