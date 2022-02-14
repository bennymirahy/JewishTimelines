import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
    login(username, password){
        return post('/api/login', {username: username, password: password});
    },
    logout(){
        return post('/api/logout');
    },
    whoami(){
        return get('/api/whoami');
    },
    add_todo(newtask){
        return post('/api/add_todo', {new_task: newtask});
    },
    list_todos(){
        return get('/api/list_todos');
    },
    list_events(){
        return get('/api/events');
    },
    save_event(event){
        // if(!event.id) {
        //     event.id = ++ID
        //     events.push(event)   
        // }
        // events.sort((a, b) => a.age - b.age)
        return post('/api/events/save', {event: JSON.stringify(event)})
    },
    get_event(id){
        return get(`/api/events/${id}`)
    },
    remove_event(id){
        return post(`/api/events/${id}/remove`)
    }
}
export default api;

function get(url, params){
    return axios.get(url, {params: params});
}

function post(url, params){
    var fd = new FormData();
    params = params || {}
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd);
}
