import Vue from 'vue'

var logged_user = null;

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({data: data}), 600)
  })
}

const api = {
    login(username, password){
        if(password){
            logged_user = {
                username: username,
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                notifications_enabled: true,
                permissions:{
                    ADMIN: username == 'admin',
                    STAFF: username == 'admin',
                }
            };
        }
        return mockasync(logged_user);
    },
    logout(){
        logged_user = null;
        return mockasync({});
    },
    whoami(){
        return mockasync(logged_user ? {
            authenticated: true,
            user: logged_user,
        } : {authenticated: false});
    },
    add_todo(newtask){
        return mockasync({description: newtask, done: false});
    },
    list_todos(){
        return mockasync({
            todos: [
                {description: 'Do the laundry', done: true},
                {description: 'Walk the dog', done: false}
            ]
        });
    },
    list_events(){
        return mockasync(events)
    },
    save_event(event){
        if(!event.id) {
            event.id = ++ID
            events.push(event)   
        }
        events.sort((a, b) => a.age - b.age)
        return mockasync(event)
    },
    get_event(id){
        return mockasync(events.filter(event => event.id == id)[0])
    }
};

let events = [
    {id: 1, age: 0, description: 'Joseph was born in the Mesopotamian town of Haran, on the 1st of Tammuz, to his parents Jacob and Rachel', source: 'Genesis 30:22-25', sourceAge: ''},
    {id: 2, age: 9, description: 'Rachel dies whilst giving birth to Benjamin', source: 'Genesis 35:16-19', sourceAge: 'dont know yet'},
    {id: 3, age: 17, description: 'Thrown into a pit with serpants and scorpions. Sold to a caravan of Midianites by his brothers', source: 'Genesis 37:24-28 & Shabbat 22a', sourceAge: 'Genesis 37:2'},
    {id: 4, age: 17, description: 'When the caravan passes along the to Efrat, while its way to Egypt, Joseph approaches Rachel\'s burial site. He cries out loudly and wept bitterly upon his mother\'s grave. He gets beaten and driven away for escaping', source: 'Sefer Hayashar: Book of Genesis, Vayeshev. This is commonly linked to the passage in Jeremiah 31:14, where Rachel refuses to be comforted for her children, as did Jacob in regards to Joseph (Genesis 37:35).', sourceAge: 'Genesis 37:2'},
    {id: 5, age: 18, description: 'Falsely accused of seducing Potiphar\'s wife and thrown into prison for 10 years', source: 'Genesis 39:11-20', sourceAge: 'Seder Olam Rabbah & Baal HaTurim & Pirkei DeRabbi Eliezer, 39 (Joseph was imprisoned initially for 10 years)'},
    {id: 6, age: 28, description: 'Asks 2 of Pharoh\'s imprisoned workers why they\'re melancholic and proceeds to interpret their dreams', source: 'Genesis 40:6-19', sourceAge: 'Rashi on Bereshit 40:23 (2 years were added to Joseph\'s sentence)'},
    {id: 7, age: 30, description: 'Interprets Pharoh\'s dream and comes out from prison on Rosh Hashana to become vice-roy of Egypt', source: 'Genesis 41:40-45 & Rosh Hashana 10b:10', sourceAge: 'Genesis 41:46'}
]
let ID = 5000

export default api;
