string = """""A university orientation is a place where students can learn about the university structure. The 
students that are going there are probably going on their own, willing to learn about the university that they are
interested in. Therefore the university should not worry if the students are using their phones or not. That decision
should be in the students' hands, if they want to learn, or if they just want to waste their time. Some people might 
say that using the cellphone will end up distracting the students from the important things of the orientation, 
but it can actually help the students. The university can use the easy internet connection that the students have to 
their advantage. They can post all the information of the orientation on their website, giving the students easy 
access to what they need to do on the orientation day. An orientation in a university campus might be a difficult 
place to find someone, with all the students and parents walking around. So with their cellphones the students can 
easily communicate with their friends and family. It not just helps the students, it also helps the university. 
Allowing this communication will make it easier for the students and parents to walk around the campus, Allowing the 
communication between students and parents, and making a website with the orientation will help the university a lot, 
giving the university staff less work to do, since they won’t have to be worrying about helping the students and 
parents to find the events. It can be said that even if the university gives the information online, many students 
will, instead of using the internet for the website information, use it to distract themselves. It might be true that 
after arriving at the orientations, instead of paying attention to it , many students will probably just mess around 
with their phones. While that is a problem, that should not be the university’s problem, most of the students in 
these orientations will be around eighteen years old, and at that age they should already know how to behave in
public. The students should pay attention to the orientation not because they are forced to do so, but because they 
want to learn about the university. Besides that, it is not every student that is willing to go to a university 
orientation. Probably most of the students present are there because they are interested in what they have to say. So 
the university should not worry about using cellphones during the presentations. The university claims that by 
banning cellphones, they will be giving the students the opportunities to make friends. While it might be true for 
some people, it might not work for everyone. There are many students that prefer to be by themselves, and they do 
that by distracting themselves with their cellphones. It is important to make friends, but this type  of student 
might not be the best way. By removing their phone, those students might feel insecure and embarrassed, making their 
experience not so good. Those students might prefer to make friends in an environment more calm and private. In 
conclusion, banning cellphones in university orientations is not a good idea. The students who are going to 
orientations are already old enough to know what is right and what is wrong and they are old enough to decide what 
they want to hear and to do. The students are going to an orientation to learn about the university. So taking the 
students' phones away, so they can make pay attention on the orientation or make friends,  should not be the 
university decision and concern."""

count = 0
for lines in string:
    for words in lines:
        if words == " ":
            count += 1

print(count)