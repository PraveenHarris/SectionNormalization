##Normalizaition Explanation

I attempted to solve this problem by building up my solution. Specifically, I tried to tackle the most simple normalization problems, and then tackle more complicated ones and eventually attempted to deal with all of the edge cases. This led me to start with solving the citifield and mets normalization problem.

My original normalize algorithm essentially just searched for the section_name in self.data without any preprocessing of the section and row arguments, along with no preprocessing of the data in the manifest file. With this, I easily got 1000/1000 on the mets dataset, but got -2162/1000 on the dodgers dataset.

To incorporate the dodgers dataset into my solution, I changed the structure of my dictionary as shown below and preprocessed the manifest file along witht the section and row arguments in the normalize function.

    {section number :
    	{abbreviation of section_name : 
    		[section_id , {row : row_id}]
    	}
    }

section number is the numerical values of section_name. For example, Left Field Pavilion 311 would be 311.
abbreviation of section_name is a shortened version of section_name. For example, Left Field Pavilion 311 would be lfp 311.

From a high level, my normalize algorithm finds likely sections that the section argument corresponds to, then uses string similarity to find the most likely one, and then finds the corresponding row.

I created this dictionary structure because I realized that there were different sections with the same section number, such as Field Box 36 and Reserve 36. I designed my dictionary so that sections with the same section number would be grouped together, and then I would use string similarity to determine the more likely section given the section_name. This structure helped me get 950/1000 points on the dodgers and 1000/1000 on the mets.

If I had more time, I would probably like to use regular expressions, as it is probably a cleaner and more time efficient method. I would have used it for this 2 hour period, but I don't know how to use them.

Above all, however, I believe the best way by far to solve this problem is to create a learning algorithm that can predict sections based off a much larger training dataset.


