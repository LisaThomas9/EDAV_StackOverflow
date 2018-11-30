import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/lisa/Downloads/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://stackoverflow.com/questions/tagged/r');
#time.sleep(5) # Let the user actually see something!

i = 2
j = 6
while i <= 10: 
	time.sleep(5)
	search_box = driver.find_element_by_id('questions')

	questions = search_box.find_elements_by_class_name("question-summary")
	for q in questions:
		#vote_count = q.find_element_by_class_name('vote-count-post ').text
		#view_count = q.find_element_by_class_name('views ').text 
		#ans_count = q.find_element_by_xpath("./div[1]/div[1]/div[2]/strong").text

		'''
		tag_list = []
		tags = q.find_elements_by_xpath("./div[2]/div[2]/*")
		for tag in tags:
			t = tag.text
			if(t != "r")
				tag_list.append()
		
		time = q.find_element_by_xpath("./div[2]/div[3]/div/div[1]/span").get_attribute("title").split(" ")
		date_posted = time[0]
		time_posted = time[1]
		'''

		#user = q.find_element_by_xpath('.//div[@class="user-details"]/a').text 
		#rep_score = q.find_element_by_xpath('.//div[@class="user-details"]//span[@class="reputation-score"]').text

		#print(user, rep_score)#, view_count, ans_count)

	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	next_page = driver.find_element_by_xpath('//*[@id="mainbar"]/div[6]/a['+str(j)+']')
	print(next_page.get_attribute("title"))
	next_page.click()

	i += 1
	j = 7



#driver.quit()