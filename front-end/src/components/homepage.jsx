import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import axios from "axios";
import { Image} from 'semantic-ui-react'
import UberLogo from '../images/uber-logo.png'

class HomePage extends Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }
    bookAppointment=()=>{
        if(this.props.userProfile) {
            this.props.history.push(`/dashboard`);
            this.props.dispatch({type: 'activeMenuItem', data: "Dashboard"});

        }else{
            this.props.history.push(`/login`);
            this.props.dispatch({type: 'activeMenuItem', data: "Login"});
        }
    }
    registration=()=>{
        this.props.history.push(`/register`);
        this.props.dispatch({type: 'activeMenuItem', data: "Register"});
    }

    componentDidMount() {

    }
    render() {
        return (<div className='registrationForm-Container'>
            <Image style={{margin:'auto'}}  src={UberLogo} size='large' />
            <div className='home-container'>UBER SANTÉ</div>
            <div className='home-second-container'><p>Would you like to see a Doctor?</p><a onClick={this.bookAppointment}>Book your appointment Now!</a></div>
            <div className='home-third-container' onClick={this.registration}>Haven't registered to the system yet?</div>
        </div>)
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(HomePage));