import re
import random

patterns_responses = {
r".*(hello|hi).*": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
    r".*(how are you|how's it going|how do you do).*": ["I'm just a bot, but I'm here to help!", "I'm good, thank you!"],
    r".*(bye|goodbye).*": ["Goodbye! Have a great day!", "See you later! Take care!"],
    r".*(thanks|thank you).*": ["You're welcome!", "No problem!"],
    r".*(what is your name|who are you|your name).*": ["I am a chatbot created by Pranit Zambre."],
    r".*(who is pranit zambre).*": ["He is my creator."],
    r".*(whats the weather today|forecast).*": ["I'm sorry, I'm not programmed to provide weather forecasts.", "You can check the weather online!"],
    r".*(help).*": ["Sure, I can help you. Just ask me anything!", "What do you need assistance with?"],
    r".*(your age|how old are you).*": ["I don't have an age. I was created by Pranit Zambre. I am a chatbot named Angel."],
    r".*(tell me a joke|joke).*": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    r".*(what can you do|capabilities).*": ["I can answer questions, tell jokes, and provide assistance on various topics!", "I can help you with information and entertain you with jokes!"],
    r".*(favorite).*": ["I don't have favorites, but I'm here to assist you with anything you need!"],
    r".*(how to).*": ["I can provide guidance on a variety of topics. Just let me know what you're interested in learning!"],
    r".*(where are you from|birthplace).*": ["I come from the depths of the internet!", "I am a citizen of the digital realm!"],
    r".*(who created you|your creator).*": ["I was created by a team of developers at OpenAI!", "My creators are talented engineers who built me to assist you!"],
    r".*(how do you work|how are you programmed).*": ["I work by processing your input and matching it with predefined patterns!", "I'm programmed to understand natural language and respond accordingly!"],
    r".*(thank you|thanks).*": ["You're welcome!", "Glad I could assist you!"],
    r".*(good morning|good afternoon|good evening).*": ["Good morning/afternoon/evening to you too!", "Hello!"],
    r".*(how's the weather today|what's the weather like).*": ["I'm sorry, I can't provide weather updates. You can check a weather website or app!"],
    r".*(can you sing|sing a song).*": ["I'm better at chatting than singing! But here's a virtual tune: la la la!"],
    r".*(are you human).*": ["No, I'm a chatbot!"],
    r".*(I'm bored).*": ["Let's chat! Tell me about your day."],
    r".*(pizza|food).*": ["I love pizza! What's your favorite topping?"],
    r".*(movie|film).*": ["Movies are great! What's your favorite genre?"],
    r".*(sports|favorite sport).*": ["Sports are exciting! Do you have a favorite team?"],
    r".*(pet|animal).*": ["Pets are adorable! Do you have any pets?"],
    r".*(book|reading).*": ["Books are fantastic! What's the last book you read?"],
    r".*(music|favorite band).*": ["Music is wonderful! What's your favorite genre?"],
    r".*(coding|programming).*": ["Coding is cool! What programming languages do you know?"],
    r".*(travel|favorite destination).*": ["Traveling is fun! Where's your dream destination?"],
    r".*(coffee|tea).*": ["I don't drink, but I hear coffee and tea are popular choices!"],
    r".*(gaming|favorite game).*": ["Gaming is fun! What's your favorite video game?"],
    r".*(exercise|workout).*": ["Exercise is important for staying healthy! What's your favorite workout?"],
    r".*(technology|favorite gadget).*": ["Technology is amazing! What's your favorite gadget?"],
    r".*(art|favorite artist).*": ["Art is beautiful! Who's your favorite artist?"],
    r".*(science|favorite scientist).*": ["Science is fascinating! Who's your favorite scientist?"],
    r".*(history|favorite historical figure).*": ["History is rich! Who's your favorite historical figure?"],
    r".*(space|favorite planet).*": ["Space is vast! What's your favorite planet?"],
    r".*(love|relationship).*": ["Love is wonderful! What's your idea of a perfect date?"],
    r".*(money|finance).*": ["Money matters! What's your best financial tip?"],
    r".*(politics|favorite politician).*": ["Politics can be complex! What's your take on current events?"],
    r".*(health|wellness).*": ["Health is important! What's your favorite healthy habit?"],
    r".*(education|learning).*": ["Education is key! What's something new you've learned recently?"],
    r".*(philosophy|favorite philosopher).*": ["Philosophy is thought-provoking! Who's your favorite philosopher?"],
    r".*(hobby|favorite pastime).*": ["Hobbies are great! What's your favorite hobby?"],
    r".*(friend|best friend).*": ["Friends are important! What qualities do you value in a friend?"],
    r".*(family|family member).*": ["Family is everything! Who's your favorite family member?"],
    r".*(dream|goal).*": ["Dream big! What's your ultimate goal?"],
    r".*(vacation|dream vacation).*": ["Vacations are relaxing! Where's your dream vacation spot?"],
    r".*(fear|biggest fear).*": ["Facing fears makes us stronger! What's your biggest fear?"],
    r".*(stress|relaxation).*": ["Stress management is key! How do you unwind after a long day?"],
    r".*(random).*": ["Life is full of surprises! What's something unexpected that happened to you recently?"],
    r".*(inspiration|motivation).*": ["Inspiration is everywhere! What motivates you to keep going?"],
    r".*(future|vision).*": ["The future is exciting! What's your vision for the future?"],
    r".*(advice|best advice).*": ["Good advice is priceless! What's the best advice you've ever received?"],
    r".*(challenges|overcome).*": ["Challenges make us stronger! How do you overcome obstacles?"],
    r".*(music|song).*": ["Music is therapeutic! What's your favorite song?"],
    r".*(movie|film).*": ["Movies are entertaining! What's the last movie you watched?"],
    r".*(food|cuisine).*": ["Food is delicious! What's your favorite cuisine?"],
    r".*(holiday|favorite holiday).*": ["Holidays are festive! What's your favorite holiday?"],
    r".*(technology|favorite gadget).*": ["Technology is amazing! What's your favorite gadget?"],
    r".*(nature|favorite outdoor activity).*": ["Nature is beautiful! What's your favorite outdoor activity?"],
    r".*(culture|favorite tradition).*": ["Culture is rich! What's your favorite cultural tradition?"],
    r".*(language|speak).*": ["Languages open doors! Do you speak any other languages?"],
    r".*(achievement|proudest moment).*": ["Achievements are worth celebrating! What's your proudest moment?"],
    r".*(memory|favorite memory).*": ["Memories are precious! What's your favorite memory?"],
    r".*(creativity|inspire).*": ["Creativity is limitless! What inspires your creativity?"],
    r".*(happiness|secret to happiness).*": ["Happiness is a journey! What's your secret to staying happy?"],
    r".*(dreams|interpret).*": ["Dreams are mysterious! Do you try to interpret your dreams?"],
    r".*(pets|favorite animal).*": ["Pets bring joy! What's your favorite animal?"],
    r".*(games|favorite board game).*": ["Games are fun! What's your favorite board game?"],
    r".*(social media|favorite platform).*": ["Social media keeps us connected! What's your favorite platform?"],
    r".*(self-improvement|work on yourself).*": ["Self-improvement is important! What aspect of yourself are you working on?"],
    r".*(fun fact|interesting fact).*": ["Fun facts are fascinating! What's an interesting fact you know?"],
    r".*(motivation|inspire).*": ["Motivation is key! What inspires you to reach your goals?"],
    r".*(magic|believe in magic).*": ["Magic is everywhere! Do you believe in magic?"],
    r".*(positivity|spread positivity).*": ["Positivity is contagious! How do you spread positivity?"],
    r".*(positivity|spread positivity).*": ["Positivity is contagious! How do you spread positivity?"],
    r".*(habits|good habits).*": ["Good habits lead to success! What's a good habit you practice?"],
    r".*(nature|favorite outdoor activity).*": ["Nature is beautiful! What's your favorite outdoor activity?"],
    r".*(culture|favorite tradition).*": ["Culture is rich! What's your favorite cultural tradition?"],
    r".*(language|speak).*": ["Languages open doors! Do you speak any other languages?"],
    r".*(achievement|proudest moment).*": ["Achievements are worth celebrating! What's your proudest moment?"],
    r".*(memory|favorite memory).*": ["Memories are precious! What's your favorite memory?"],
    r".*(creativity|inspire).*": ["Creativity is limitless! What inspires your creativity?"],
    r".*(happiness|secret to happiness).*": ["Happiness is a journey! What's your secret to staying happy?"],
    r".*(dreams|interpret).*": ["Dreams are mysterious! Do you try to interpret your dreams?"],
    r".*(pets|favorite animal).*": ["Pets bring joy! What's your favorite animal?"],
    r".*(games|favorite board game).*": ["Games are fun! What's your favorite board game?"],
    r".*(social media|favorite platform).*": ["Social media keeps us connected! What's your favorite platform?"],
    r".*(self-improvement|work on yourself).*": ["Self-improvement is important! What aspect of yourself are you working on?"],
    r".*(fun fact|interesting fact).*": ["Fun facts are fascinating! What's an interesting fact you know?"],
    r".*(motivation|inspire).*": ["Motivation is key! What inspires you to reach your goals?"],
    r".*(magic|believe in magic).*": ["Magic is everywhere! Do you believe in magic?"],
    r".*(positivity|spread positivity).*": ["Positivity is contagious! How do you spread positivity?"],
    r".*(habits|good habits).*": ["Good habits lead to success! What's a good habit you practice?"],
    r".*(hobbies|interests).*": ["Hobbies make life interesting! What are your hobbies or interests?"],
    r".*(education|learning).*": ["Education is important! What's something new you've learned recently?"],
    r".*(dream job|ideal job).*": ["Dream jobs are exciting! What's your ideal job?"],
    r".*(dream house|ideal house).*": ["Dream houses come in all shapes and sizes! What's your ideal house like?"],
    r".*(dream car|ideal car).*": ["Dream cars are cool! What's your dream car?"],
    r".*(bucket list|things to do before you die).*": ["Bucket lists are fun! What's on your bucket list?"],
    r".*(weekend plans|plans for the weekend).*": ["Weekends are for relaxation! What are your plans?"],
    r".*(morning routine|start your day).*": ["Morning routines set the tone! How do you start your day?"],
    r".*(evening routine|end your day).*": ["Evening routines help unwind! How do you end your day?"],
    r".*(exercise routine|workout routine).*": ["Exercise routines keep you fit! What's your workout routine?"],
    r".*(healthy habits|stay healthy).*": ["Healthy habits lead to a healthy life! What healthy habits do you practice?"],
    r".*(productivity tips|be productive).*": ["Productivity tips help you get things done! What's your favorite productivity tip?"],
    r".*(stress relief|relax).*": ["Stress relief techniques are important! How do you relax and unwind?"],
    r".*(mindfulness|practice mindfulness).*": ["Mindfulness helps stay present! How do you practice mindfulness?"],
    r".*(goal setting|set goals).*": ["Goal setting is important for success! How do you set and achieve your goals?"],
    r".*(time management|manage time).*": ["Time management is key to productivity! How do you manage your time effectively?"],
    r".*(work-life balance|balance).*": ["Work-life balance is essential for well-being! How do you maintain balance in your life?"],
    r".*(motivation|stay motivated).*": ["Motivation keeps you going! How do you stay motivated?"],
    r".*(positive mindset|think positive).*": ["A positive mindset is powerful! How do you maintain a positive outlook?"],
    r".*(inspiration|inspire).*": ["Inspiration is everywhere! What inspires you to keep going?"],
    r".*(creativity|be creative).*": ["Creativity is limitless! How do you nurture your creativity?"],
    r".*(imagination|imagine).*": ["Imagination has no bounds! What do you imagine for the future?"],
    r".*(life purpose|find purpose).*": ["Finding purpose gives meaning to life! How do you discover your life purpose?"],
    r".*(legacy|leave a legacy).*": ["Leaving a legacy is impactful! How do you want to be remembered?"],
    r".*(personal growth|grow).*": ["Personal growth is a journey! How do you work on personal development?"],
    r".*(relationships|build relationships).*": ["Relationships are important! How do you nurture your relationships?"],
    r".*(communication skills|communicate effectively).*": ["Communication skills are essential! How do you improve communication?"],
    r".*(emotional intelligence|develop emotional intelligence).*": ["Emotional intelligence is key! How do you develop emotional intelligence?"],
    r".*(leadership qualities|be a leader).*": ["Leadership qualities make a difference! How do you develop leadership skills?"],
    r".*(resilience|be resilient).*": ["Resilience is strength! How do you build resilience?"],
    r".*(gratitude|practice gratitude).*": ["Gratitude is transformative! How do you practice gratitude?"],
    r".*(kindness|be kind).*": ["Kindness is contagious! How do you spread kindness?"],
    r".*(happiness|happiness habits).*": ["Happiness is a choice! What habits contribute to your happiness?"],
    r".*(mindset|positive mindset).*": ["A positive mindset is powerful! How do you maintain a positive outlook?"],
    r".*(success|secrets to success).*": ["Success leaves clues! What habits contribute to your success?"],
    r".*(motivation|stay motivated).*": ["Motivation keeps you going! What motivates you to reach your goals?"],
    r".*(creativity|boost creativity).*": ["Creativity is limitless! How do you spark creativity?"],
    r".*(mindfulness|practice mindfulness).*": ["Mindfulness keeps you present! How do you practice mindfulness?"],
    r".*(self-care|take care of yourself).*": ["Self-care is important! How do you practice self-care?"],
    r".*(stress|stress management).*": ["Stress management is key! How do you cope with stress?"],
    r".*(wellness|well-being).*": ["Wellness is holistic! How do you prioritize your well-being?"],
    r".*(productivity|be productive).*": ["Productivity leads to success! How do you maximize productivity?"],
    r".*(balance|work-life balance).*": ["Balance is essential! How do you maintain work-life balance?"],
    r".*(habits|healthy habits).*": ["Healthy habits lead to a healthy life! What healthy habits do you practice?"],
    r".*(goals|set goals).*": ["Goals give direction! How do you set and achieve your goals?"],
    r".*(motivation|find motivation).*": ["Motivation keeps you going! What motivates you to pursue your goals?"],
    r".*(positivity|positive mindset).*": ["Positivity is powerful! How do you cultivate a positive mindset?"],
    r".*(inspiration|inspire).*": ["Inspiration sparks creativity! What inspires you in your life?"],
    r".*(personal growth|grow).*": ["Personal growth is continuous! How do you invest in yourself?"],
    r".*(relationship|build relationships).*": ["Relationships are meaningful! How do you nurture your relationships?"],
    r".*(communication|communicate effectively).*": ["Communication is key! How do you improve your communication skills?"],
    r".*(empathy|practice empathy).*": ["Empathy fosters connection! How do you practice empathy in your life?"],
    r".*(leadership|leadership qualities).*": ["Leadership is influential! How do you develop your leadership skills?"],
    r".*(resilience|be resilient).*": ["Resilience is strength! How do you cultivate resilience in tough times?"],
    r".*(gratitude|practice gratitude).*": ["Gratitude is transformative! How do you cultivate gratitude in your life?"],
    r".*(kindness|be kind).*": ["Kindness is contagious! How do you spread kindness to others?"],
    r".*(happiness|happiness habits).*": ["Happiness is a journey! What habits contribute to your happiness?"],
    r".*(mindset|positive mindset).*": ["A positive mindset is powerful! How do you maintain a positive outlook?"],
    r".*(success|secrets to success).*": ["Success leaves clues! What habits contribute to your success?"],
    r".*(motivation|stay motivated).*": ["Motivation keeps you going! What motivates you to reach your goals?"],
    r".*(creativity|boost creativity).*": ["Creativity is limitless! How do you spark creativity?"],
    r".*(mindfulness|practice mindfulness).*": ["Mindfulness keeps you present! How do you practice mindfulness?"],
    r".*(self-care|take care of yourself).*": ["Self-care is important! How do you practice self-care?"],
    r".*(stress|stress management).*": ["Stress management is key! How do you cope with stress?"],
    r".*(wellness|well-being).*": ["Wellness is holistic! How do you prioritize your well-being?"],
    r".*(productivity|be productive).*": ["Productivity leads to success! How do you maximize productivity?"],
    r".*(balance|work-life balance).*": ["Balance is essential! How do you maintain work-life balance?"],
    r".*(habits|healthy habits).*": ["Healthy habits lead to a healthy life! What healthy habits do you practice?"],
    r".*(goals|set goals).*": ["Goals give direction! How do you set and achieve your goals?"],
    r".*(motivation|find motivation).*": ["Motivation keeps you going! What motivates you to pursue your goals?"],
    r".*(positivity|positive mindset).*": ["Positivity is powerful! How do you cultivate a positive mindset?"],
    r".*(inspiration|inspire).*": ["Inspiration sparks creativity! What inspires you in your life?"],
    r".*(personal growth|grow).*": ["Personal growth is continuous! How do you invest in yourself?"],
    r".*(relationship|build relationships).*": ["Relationships are meaningful! How do you nurture your relationships?"],
    r".*(communication|communicate effectively).*": ["Communication is key! How do you improve your communication skills?"],
    r".*(empathy|practice empathy).*": ["Empathy fosters connection! How do you practice empathy in your life?"],
    r".*(leadership|leadership qualities).*": ["Leadership is influential! How do you develop your leadership skills?"],
    r".*(resilience|be resilient).*": ["Resilience is strength! How do you cultivate resilience in tough times?"],
    r".*(gratitude|practice gratitude).*": ["Gratitude is transformative! How do you cultivate gratitude in your life?"],
    r".*(kindness|be kind).*": ["Kindness is contagious! How do you spread kindness to others?"],
    r".*(happiness|happiness habits).*": ["Happiness is a journey! What habits contribute to your happiness?"],
    r".*(mindset|positive mindset).*": ["A positive mindset is powerful! How do you maintain a positive outlook?"],
    r".*(success|secrets to success).*": ["Success leaves clues! What habits contribute to your success?"],
    r".*(motivation|stay motivated).*": ["Motivation keeps you going! What motivates you to reach your goals?"],
    r".*(creativity|boost creativity).*": ["Creativity is limitless! How do you spark creativity?"],
    r".*(mindfulness|practice mindfulness).*": ["Mindfulness keeps you present! How do you practice mindfulness?"],
    r".*(self-care|take care of yourself).*": ["Self-care is important! How do you practice self-care?"],
    r".*(stress|stress management).*": ["Stress management is key! How do you cope with stress?"],
    r".*(wellness|well-being).*": ["Wellness is holistic! How do you prioritize your well-being?"],
    r".*(productivity|be productive).*": ["Productivity leads to success! How do you maximize productivity?"],
    r".*(balance|work-life balance).*": ["Balance is essential! How do you maintain work-life balance?"],
    r".*(habits|healthy habits).*": ["Healthy habits lead to a healthy life! What healthy habits do you practice?"],
    r".*(goals|set goals).*": ["Goals give direction! How do you set and achieve your goals?"],
    r".*(motivation|find motivation).*": ["Motivation keeps you going! What motivates you to pursue your goals?"],
    r".*(positivity|positive mindset).*": ["Positivity is powerful! How do you cultivate a positive mindset?"],
    r".*(inspiration|inspire).*": ["Inspiration sparks creativity! What inspires you in your life?"],
    r".*(personal growth|grow).*": ["Personal growth is continuous! How do you invest in yourself?"],
    r".*(relationship|build relationships).*": ["Relationships are meaningful! How do you nurture your relationships?"],
    r".*(communication|communicate effectively).*": ["Communication is key! How do you improve your communication skills?"],
    r".*(empathy|practice empathy).*": ["Empathy fosters connection! How do you practice empathy in your life?"],
    r".*(leadership|leadership qualities).*": ["Leadership is influential! How do you develop your leadership skills?"],
    r".*(resilience|be resilient).*": ["Resilience is strength! How do you cultivate resilience in tough times?"],
    r".*(gratitude|practice gratitude).*": ["Gratitude is transformative! How do you cultivate gratitude in your life?"],
    r".*(kindness|be kind).*": ["Kindness is contagious! How do you spread kindness to others?"],
    r".*(happiness|happiness habits).*": ["Happiness is a journey! What habits contribute to your happiness?"],
    r".*(mindset|positive mindset).*": ["A positive mindset is powerful! How do you maintain a positive outlook?"],
    r".*(success|secrets to success).*": ["Success leaves clues! What habits contribute to your success?"],
    r".*(motivation|stay motivated).*": ["Motivation keeps you going! What motivates you to reach your goals?"],
    r".*(creativity|boost creativity).*": ["Creativity is limitless! How do you spark creativity?"],
    r".*(mindfulness|practice mindfulness).*": ["Mindfulness keeps you present! How do you practice mindfulness?"],
    r".*(self-care|take care of yourself).*": ["Self-care is important! How do you practice self-care?"],
    r".*(stress|stress management).*": ["Stress management is key! How do you cope with stress?"],
    r".*(wellness|well-being).*": ["Wellness is holistic! How do you prioritize your well-being?"],
    r".*(productivity|be productive).*": ["Productivity leads to success! How do you maximize productivity?"],
    r".*(balance|work-life balance).*": ["Balance is essential! How do you maintain work-life balance?"],
    r".*(habits|healthy habits).*": ["Healthy habits lead to a healthy life! What healthy habits do you practice?"],
    r".*(goals|set goals).*": ["Goals give direction! How do you set and achieve your goals?"],
    r".*(motivation|find motivation).*": ["Motivation keeps you going! What motivates you to pursue your goals?"],
    r".*(positivity|positive mindset).*": ["Positivity is powerful! How do you cultivate a positive mindset?"],
    r".*(inspiration|inspire).*": ["Inspiration sparks creativity! What inspires you in your life?"],
    r".*(personal growth|grow).*": ["Personal growth is continuous! How do you invest in yourself?"],
    r".*(relationship|build relationships).*": ["Relationships are meaningful! How do you nurture your relationships?"],
    r".*(communication|communicate effectively).*": ["Communication is key! How do you improve your communication skills?"],
    r".*(empathy|practice empathy).*": ["Empathy fosters connection! How do you practice empathy in your life?"],
    r".*(leadership|leadership qualities).*": ["Leadership is influential! How do you develop your leadership skills?"],
    r".*(resilience|be resilient).*": ["Resilience is strength! How do you cultivate resilience in tough times?"],
    r".*(gratitude|practice gratitude).*": ["Gratitude is transformative! How do you cultivate gratitude in your life?"],
    r".*(kindness|be kind).*": ["Kindness is contagious! How do you spread kindness to others?"],
    r".*(happiness|happiness habits).*": ["Happiness is a journey! What habits contribute to your happiness?"],
    r".*(mindset|positive mindset).*": ["A positive mindset is powerful! How do you maintain a positive outlook?"],
    r".*(success|secrets to success).*": ["Success leaves clues! What habits contribute to your success?"],
    r".*(motivation|stay motivated).*": ["Motivation keeps you going! What motivates you to reach your goals?"],
    r".*(creativity|boost creativity).*": ["Creativity is limitless! How do you spark creativity?"],
    r".*(mindfulness|practice mindfulness).*": ["Mindfulness keeps you present! How do you practice mindfulness?"],
    r".*(self-care|take care of yourself).*": ["Self-care is important! How do you practice self-care?"],
    r".*(stress|stress management).*": ["Stress management is key! How do you cope with stress?"],
    r".*(wellness|well-being).*": ["Wellness is holistic! How do you prioritize your well-being?"],
    r".*(productivity|be productive).*": ["Productivity leads to success! How do you maximize productivity?"],
    r".*(balance|work-life balance).*": ["Balance is essential! How do you maintain work-life balance?"],
    r".*(habits|healthy habits).*": ["Healthy habits lead to a healthy life! What healthy habits do you practice?"],
    r".*(goals|set goals).*": ["Goals give direction! How do you set and achieve your goals?"],
    r".*(motivation|find motivation).*": ["Motivation keeps you going! What motivates you to pursue your goals?"],
    r".*(positivity|positive mindset).*": ["Positivity is powerful! How do you cultivate a positive mindset?"],
    r".*(inspiration|inspire).*": ["Inspiration sparks creativity! What inspires you in your life?"],
    r".*(personal growth|grow).*": ["Personal growth is continuous! How do you invest in yourself?"],
    r".*(relationship|build relationships).*": ["Relationships are meaningful! How do you nurture your relationships?"],
    r".*(communication|communicate effectively).*": ["Communication is key! How do you improve your communication skills?"],
    r".*(empathy|practice empathy).*": ["Empathy fosters connection! How do you practice empathy in your life?"],
    r".*(leadership|leadership qualities).*": ["Leadership is influential! How do you develop your leadership skills?"],
    r".*(resilience|be resilient).*": ["Resilience is strength! How do you cultivate resilience in tough times?"],
    r".*(gratitude|practice gratitude).*": ["Gratitude is transformative! How do you cultivate gratitude in your life?"],
    r".*(kindness|be kind).*": ["Kindness is contagious! How do you spread kindness to others?"],
    r".*(happiness|happiness habits).*": ["Happiness is a journey! What habits contribute to your happiness?"],
    r".*(mindset|positive mindset).*": ["A positive mindset is powerful! How do you maintain a positive outlook?"],
    r".*(success|secrets to success).*": ["Success leaves clues! What habits contribute to your success?"],
    r".*(motivation|stay motivated).*": ["Motivation keeps you going! What motivates you to reach your goals?"],
    r".*(creativity|boost creativity).*": ["Creativity is limitless! How do you spark creativity?"],
    r".*(mindfulness|practice mindfulness).*": ["Mindfulness keeps you present! How do you practice mindfulness?"],
    r".*(self-care|take care of yourself).*": ["Self-care is important! How do you practice self-care?"],
    r".*(stress|stress management).*": ["Stress management is key! How do you cope with stress?"],
    r".*(wellness|well-being).*": ["Wellness is holistic! How do you prioritize your well-being?"],
    r".*(productivity|be productive).*": ["Productivity leads to success! How do you maximize productivity?"],
    r".*(balance|work-life balance).*": ["Balance is essential! How do you maintain work-life balance?"],
    r".*(habits|healthy habits).*": ["Healthy habits lead to a healthy life! What healthy habits do you practice?"],
    r".*(goals|set goals).*": ["Goals give direction! How do you set and achieve your goals?"],
    r".*(motivation|find motivation).*": ["Motivation keeps you going! What motivates you to pursue your goals?"],
    r".*(positivity|positive mindset).*": ["Positivity is powerful! How do you cultivate a positive mindset?"],
    r".*(inspiration|inspire).*": ["Inspiration sparks creativity! What inspires you in your life?"],
    r".*(personal growth|grow).*": ["Personal growth is continuous! How do you invest in yourself?"],
    r".*(relationship|build relationships).*": ["Relationships are meaningful! How do you nurture your relationships?"],
    r".*(communication|communicate effectively).*": ["Communication is key! How do you improve your communication skills?"],
    r".*(empathy|practice empathy).*": ["Empathy fosters connection! How do you practice empathy in your life?"],
    r".*(leadership|leadership qualities).*": ["Leadership is influential! How do you develop your leadership skills?"],
    r".*(resilience|be resilient).*": ["Resilience is strength! How do you cultivate resilience in tough times?"],
    r".*(gratitude|practice gratitude).*": ["Gratitude is transformative! How do you cultivate gratitude in your life?"],
    r".*(kindness|be kind).*": ["Kindness is contagious! How do you spread kindness to others?"],
    r".*(happiness|happiness habits).*": ["Happiness is a journey! What habits contribute to your happiness?"],
    r".*(mindset|positive mindset).*": ["A positive mindset is powerful! How do you maintain a positive outlook?"],
    r".*(success|secrets to success).*": ["Success leaves clues! What habits contribute to your success?"],
    r".*(motivation|stay motivated).*": ["Motivation keeps you going! What motivates you to reach your goals?"],
    r".*(creativity|boost creativity).*": ["Creativity is limitless! How do you spark creativity?"],
    r".*(mindfulness|practice mindfulness).*": ["Mindfulness keeps you present! How do you practice mindfulness?"],
    r".*(self-care|take care of yourself).*": ["Self-care is important! How do you practice self-care?"]
}

def respond_to_user_input(user_input):
    for pattern, responses in patterns_responses.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return "I'm sorry, I didn't understand that. Please be more clear."


def main():
    print("Welcome to the Angel Chatbot by Pranit Zambre! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break

        response = respond_to_user_input(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()