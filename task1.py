from collections import Counter


def parse_line(line):
    year = line[13:17]
    month = line[18:21]
    success = True if line[193:194] == 'S' else False
    return dict(year=year, month=month, success=success, count=1)


def parse_records(stream):
    records = []
    for line in stream.readlines()[2:]:
        record = parse_line(line)
        if record['year'] == '    ':
            records[-1]['count'] += 1
        else:
            records.append(record)
    return records


def filter_records(records, success):
    if success is None:
        return records
    filtered_records = []
    for record in records:
        if record['success'] == success:
            filtered_records.append(record)
    return filtered_records


def group_by(stream, field, success=None):
    records = parse_records(stream)
    records = filter_records(records, success)
    counter = Counter()
    for record in records:
        if field == 'year':
            counter[record['year']] += record['count']
        else:
            counter[record['month']] += record['count']
    return dict(counter)
