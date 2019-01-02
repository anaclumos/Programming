import time
#prime_num.txt의 소수 불러오기
def get_prime_number():
	prime_num_txt = open('prime_num.txt', 'r')
	prime_num_str = prime_num_txt.read()
	return prime_num_str.split(',')
	#검증범위 입력받기
def question():
	print('2보다 큰 모든 짝수를 두 소수의 합으로 나타낼 수 있다는것이 골드바흐의 추측.')
	print('n이하의 짝수에 대하여 골드바흐의 추측 증명')
	print('n값입력')
	return int(input())
	#goldbach_test_list 를  boolean변수 이용하여 만듦
def get_goldbach_test_list(num):
	test_list = [True,False]*(int(num/2))
	test_list[0]=False
	test_list[2]=False
	test_list.append(True)
	return test_list
def main():
	global start_time
	max_range=question()
	start_time=time.time()
	prime_num_list=get_prime_number()
	prime_num_list=list(map(lambda x: int(x), prime_num_list))
	#prime_num_list 에서 max_range_num  이상 잘라냄
	prime_num_list=list(filter(lambda x:x<=max_range, prime_num_list))
	goldbach_test_list=get_goldbach_test_list(max_range)
	for prime1 in prime_num_list:
		if sum(goldbach_test_list)==0:
			break
			#합이 0이면 중단
		for prime2 in prime_num_list:
			if prime1+prime2<=max_range:
				goldbach_test_list[prime1+prime2]=False
			print('{0}={1}+{2}'.format(prime1+prime2,prime1,prime2))
	print('{0}개의 오류가 발견됨'.format(sum(goldbach_test_list)))
	print('경과시간:{0}'.format(time.time()-start_time))
main()