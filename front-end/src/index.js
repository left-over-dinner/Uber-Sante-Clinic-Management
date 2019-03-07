import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import {createStore, combineReducers} from 'redux';
import {Provider} from 'react-redux'
import {BrowserRouter} from "react-router-dom";
import Reducers from './reducers'


const reducers = combineReducers({
    Reducers,
});
const store = createStore(reducers);
if(localStorage.jwtToken) {
    store.dispatch({type: 'addUserProfile', data: JSON.parse(localStorage.getItem('jwtToken'))})
}

ReactDOM.render(
<Provider store={store}>
    <BrowserRouter>
    <App />
    </BrowserRouter>
    </Provider>
    , document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
