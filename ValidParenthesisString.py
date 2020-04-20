
Class Solution:
	def checkValidString(self,s: str) -> boo:
		left=right=0
		for i in range(len(s)):
			if s[i] in "(*":
				left+=1
			else:
				left-=1
			if left<0:
				return False
			if s[len(s)-1-i)] in "*)":
				right+=1
			else:
				right-=1
			if right<0:
				return False
		return True
 