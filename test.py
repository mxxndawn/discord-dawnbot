from const  import get_value

# instance1의 spac를 가져오기
instance1_spac = get_value('aws_info', 'instance', 'instance1', 'spac')
print("Instance 1 Spac:", instance1_spac)

# instance2의 cpu를 가져오기
instance2_cpu = get_value('aws_info', 'instance', 'instance2', 'cpu')
print("Instance 2 CPU:", instance2_cpu)