# weather_gov_api_lib
Simple python library written in python for interfacing with the weather.gov api page. This is still a work in progress.

Some features currently available:

find a element by a parameter. returns string.
  get_param(a,b,c)
  
  a represents the index of the datapoint in the json resposnse.
  b represents the dictionary file you want to search from. In this case the properties section.
  c represents the name that it searches for. 


get the properties section of the JSON returns a dict
  get_properties(a)
  
  a represents the full JSON response from the api.weather.gov page. 
  this function is pretty essential because most of the other functions use the output of this for input.

get all of the calues of a certain parameter in the entire response. returns a list with all the values in it.
  get_all_params(a,b)
  
  a represents the dictionary you are secrhing from. give it the properties dictionary.
  b represents the term that is being searched for e.g "startTime"

get the amount of datapoints returns a integer
  get_largest_number(a)
  
  a represents the dictionary file it is searching in. give it the properties dictionary. 

get only 1 value from the entire set. 
  get_number(a,b)
  
  a represents the number inside each datapoint.
  b represents the dictionary. give it the properties dictionary.
  

FYI the data main website is weather.gov. more can be read there. 
Their API can be used without a api key. Being able to use a api without limitations or registeration is a privlege. Make sure not to flood the api endpoint.
