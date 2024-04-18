from const  import find_element_with_key


# instance1의 spac를 가지는 요소 찾기
instance1_sp_element = find_element_with_key('aws_info', 'spac', 'instance', 'instance1')
print("Instance 1 Spac Element:", instance1_sp_element)

# instance2의 cpu를 가지는 요소 찾기
instance2_cpu_element = find_element_with_key('aws_info', 'cpu', 'instance', 'instance2')
print("Instance 2 CPU Element:", instance2_cpu_element)