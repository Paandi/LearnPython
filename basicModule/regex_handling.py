import re

#Functions Available
#findall(regex,str) -- return all occurence value
#search(regex,str)  -- return tuple of first match start and end
#split(regex,split) -- split string into a list                  
#sub(old,new,str) --replace old regex to new value
#string
#span

re.search('test', 'TeSt', re.IGNORECASE)
re.match('test', 'TeSt', re.IGNORECASE)
re.sub('test', 'xxxx', 'Testing', flags=re.IGNORECASE)


input_str = "Hi, I am DCP. I am leari'ning python regular expression. Regex is very useful in serach and filter needs." 

---- Finding the number of occurence

is_count=len(re.findall("Is|am",input_str,flags=re.I))     --- output 3

--same as above
is_count=len(re.findall("Is|am",input_str,flags=re.IGNORECASE))


---- getting first start and end position

x=re.search("DC",input_str)      -- if match then start and end pos of regex,not full word Else None
print(x.start)
print(x.end)

if x is None:
	print("not matched")
else:
	print("matched")
	
	

------ replacing value

update_str=re.sub('learining','learning',input_str)    --doesn't change in existing

str_to_line=re.split('\.',input_str)    -- regex excluded.

