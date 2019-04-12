import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Icon, Form} from 'semantic-ui-react'
import '../appointment.css'
import axios from "axios";
import {Redirect} from "react-router";
import { Modal } from 'antd';
import {appointments} from "./options";
import _ from "lodash";
import moment from 'moment'
import {TimeSlotConverter} from "./calculator";

const myConverter = new TimeSlotConverter();
const confirm = Modal.confirm;

var cardOption=[];
var appointmentTypeOptions = [
    {key: 1, value: 'Walk-In', text: 'Walk-In (20min)'},
    {key: 2, value: 'Annual Checkup', text: "Annual Checkup (60min)"}];

class Availability extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: false,
            slots: [],
            date: '',
            availability: '',
            type: '',
            appointments: [],
            cardNumber: '',
            appointmentType: '',
            submit:false,

        }
    }


    componentDidMount() {

    }

    removeCart=(e,id)=>{
        e.preventDefault();
        this.props.removeFromCart(id)
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
                                <span className="cal-title-time">  Slots : {myConverter.convertArray(this.props.appointments.slots).map(slotData=>{
                                    return(<div>{slotData}</div>);
                                })} </span>
                            </div>
                        </div>
                        <div className="PMC-Delete-Edit-buttons">
                            <div className="note-author" onClick={(e)=>this.removeCart(e,this.props.appointments.id)}>
                                <Icon name="trash"/> Remove From Cart
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
export default withRouter(connect(mapStateToProps)(Availability));