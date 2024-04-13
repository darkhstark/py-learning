nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3

k = len(nums1)

for i in range(len(nums1)):
	if nums1[i] == 0:
		nums1 = nums1[0:i]
		nums1.extend(nums2)
		break
	for j in range(len(nums2)):
		if nums1[i] == nums2[j]:
			nums1.insert(i, nums2[j])
			nums2.pop(j)
			j = j+1
			break
		elif nums1[i] > nums2[j]:
			nums1.insert(i-1, nums2[j])
			nums2.pop(j)
print (nums1)
