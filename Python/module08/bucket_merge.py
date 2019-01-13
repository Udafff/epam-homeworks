""" Module 08. Exercise 1 """
from aws.boto_bucket import BotoBucket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="'#### Merge a list of buckets. ####'")
    parser.add_argument('-s', metavar='BUCKET',
                        nargs='+', help='<Required> List of source bucket names.', required=True)
    parser.add_argument('-d', metavar='BUCKET',
                        help='<Required> Destination bucket name.', required=True)
    args = parser.parse_args()

    # mrg_list = [['360ea28220cc', 'ecddf9e63475', 'a00e67f319d3', 'unavailable_bucket'], '8507-49809de6aa40']
    mrg_list = [args.s, args.d]
    cls_boto = BotoBucket()

    if cls_boto.is_exist(mrg_list[1]) is not True:
        print(f'Destination bucket name "{mrg_list[1]}" is not exists. Create new bucket...')
        bucket = cls_boto.create_bucket(mrg_list[1])
        if bucket[0] is True:
            print(f'Bucket "{bucket[1]}" successfully created.')
        else:
            print('Bucket creation is failed.')
            print(bucket[1][2])
            raise SystemExit(1)

    """ Begin merge of bucket list. """
    cls_boto.merge_bucket(mrg_list)
