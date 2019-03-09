import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Icon} from 'semantic-ui-react'
import '../appointment.css'
import axios from "axios";
import {Redirect} from "react-router";

class Appointment extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loading:'false',
        }
    }

    displayAppointment=(callback)=>{
        if(this.props.userProfile) {
            let data = {
                email: this.props.userProfile.email
            }
            axios.post('http://127.0.0.1:5000/api/Appointment',data).then(
                function (response, err) {
                    console.log(response)
                    if(response.data){
                        this.setState({loading:false})
                        callback(response.data.data);
                    }
                }.bind(this)
            ).catch(error=>{
                console.log(error)
            });
            console.log('Retrieved data for Appointment.')
        }
    }

    componentDidMount() {

    }
    render() {
        if (!this.props.userProfile) {
            return (<Redirect to={'/'}/>);
        } else {
        return (
            <div className="listCal">
                <div className="cal-box">
                    <div className="cal-list">
                        <div className="cal-date">
                            <div className="cal-date-day">
                                31St Monday
                            </div>
                            <div className="cal-date-month">
                                January
                            </div>
                        </div>
                        <div className="cal-desc">
                            <div className="cal-title">
                                <span className="cal-title-des"> Xray control</span>
                                <span lassName="cal-title-time">  From 15:30 to 15:50 </span>
                            </div>
                        </div>
                        <div className="PMC-Delete-Edit-buttons">
                            <div className="note-author">
                                <Icon name="trash"/> Delete
                            </div>
                            <div className="note-author2">
                                <Icon name="edit"/> Edit
                            </div>
                        </div>
                    </div></div>
            </div>)
        }
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(Appointment));