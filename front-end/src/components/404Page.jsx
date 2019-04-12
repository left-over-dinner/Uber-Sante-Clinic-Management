import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Modal} from "antd";

var cartArray=[];
const confirm = Modal.confirm;

class ErrorPage extends Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }



    render() {

        return (<div className='registrationForm-Container'>
                 <div id="notfound">
                        <div className="notfound">
                            <div className="notfound-404">
                                <h1>4<span></span>4</h1>
                            </div>
                            <h2>Oops! Page Not Be Found</h2>
                            <p>Sorry but the page you are looking for does not exist, have been removed. name changed or
                                is temporarily unavailable</p>
                        </div>
                    </div>
             </div>)
         }

}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(ErrorPage));