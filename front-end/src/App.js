import React, { Fragment, Component } from 'react';
import './App.css';
import 'semantic-ui-css/semantic.min.css';
import 'antd/dist/antd.css';
import {Redirect } from 'react-router'
import { Route, Switch ,withRouter} from 'react-router-dom';
import HomePage from './components/homepage.jsx'
import Registration from './components/registration.jsx'
import connect from "react-redux/es/connect/connect";
import axios from 'axios'
import Navbar from './components/navbar.jsx'
import Topbar from './components/topbar.jsx'
import Login from './components/login'
import Dashboard from './components/dashboard'


class App extends Component {
    componentDidMount(){
        /*this.props.dispatch({type: 'addUserProfile', data: 'hello' });*/
    }
    render() {
        console.log(this.props.userProfile)
        return (
            <Fragment>
            <Topbar />
            <div className='main-container-app'>
            <Navbar />
            <Switch>
            <Route exact path="/" component={HomePage} />
        <Route exact path="/register" component={Registration} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/dashboard" component={Dashboard} />
        <Redirect from="*" to="/404" />
        </Switch>
        </div>
        </Fragment>
    );
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(App));
