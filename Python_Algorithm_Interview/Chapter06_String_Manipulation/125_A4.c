// 풀이 4 - C 구현

#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(char* s) {
	int bias_left = 0;
	int bias_right = 1;
	int str_len = strlen(s);

	for (int i = 0; i < str_len; i++) {
		// 스킵 포인터 처리: 영문자, 숫자인 경우에 while 문을 빠져 나옴
		while (!isalnum(s[i + bias_left])) {
			bias_left++;
			if (i + bias_left == str_len)
				return true;
		}
		while (!isalnum(s[str_len - i - bias_right])) {
			bias_right++;
		}

		// 왼쪽 비교 포인터가 오른쪽 비교 포인터를 지나친 경우
		if (i + bias_left >= str_len - i - bias_right)
			break;

		if (tolower(s[i + bias_left]) != tolower(s[str_len - i - bias_right]))
			return false;
	}
	return true;
}

int main(int argc, char* argv[]) {
	char s[] = "A man, a plan, a canal: Panama";
	printf("%s\n", isPalindrome(s)? "true" : "false");

	char s2[] = "race a car";
	printf("%s\n", isPalindrome(s2)? "true" : "false");
}
