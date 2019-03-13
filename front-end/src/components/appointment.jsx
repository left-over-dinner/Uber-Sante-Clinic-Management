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
                                {this.props.appointments.date}
                            </div>
                            <div className="cal-date-month">
                            </div>
                        </div>
                        <div className="cal-desc">
                            <div className="cal-title">
                                <span className="cal-title-des"> {this.props.appointments.appointment_type}</span>
                                <span lassName="cal-title-time">  Slots : {this.props.appointments.slots} </span>
                            </div>
                        </div>
                        <div className="PMC-Delete-Edit-buttons">
                            {/*<div className="note-author">
                                <Icon name="trash"/> Delete
                            </div>
                            <div className="note-author2">
                                <Icon name="edit"/> Edit
                            </div>*/}
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