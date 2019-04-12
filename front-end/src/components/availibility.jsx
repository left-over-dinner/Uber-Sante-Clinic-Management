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
    delete=()=>{
        let props = this.props;
        let data = this.props.availability;
        confirm({
    title: 'Are you sure to delete this availability?',
    content: 'Note that this operation will delete permanently.',
    okText: 'Delete',
    okType: 'danger',
    cancelText: 'Cancel',
    onOk() {
        console.log(data)
        axios.delete('http://127.0.0.1:5000/api/Availability',{data} ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        props.getAvailabilities();
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    },
  });
    }
    addAppointment=(e,data)=>{
        e.preventDefault();
        console.log(data)
        var this1= this;
        let array =[];
        data.slots.map(slotData=>{
            let locationIndex = _.findIndex(appointments, function (o) {
                                        return o.value === slotData;
                                    });
            let arr= {key: appointments[locationIndex].key, value: appointments[locationIndex].value, text: appointments[locationIndex].text}
                            array.push(arr);

        })
        this.setState({appointments: array});
        this.setState({date: data.date});
        this.setState({availability: data})
        this.setState({slots: ''});
        this.setState({type: 'add'});
        this.setState({cardNumber: ""})
        this.setState({appointmentType: ''})
        axios.get('http://127.0.0.1:5000/api/Patient').then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                       console.log(response.data)
                        cardOption=[];
                        response.data.data.map(patientData=>{
                            let arr= {key: patientData.card_number, value:patientData.card_number , text: patientData.first_name+" "+patientData.last_name+" - "+ patientData.card_number}
                            cardOption.push(arr);

                        })
                        this.setState({visible:true})
                        console.log(cardOption)
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    }
    editAvailability=(e,data)=>{
        e.preventDefault();
        console.log(data)
        this.setState({visible:true})
        this.setState({date: data.date});
        this.setState({availability: data})
        this.setState({slots: data.slots});
        this.setState({type: 'edit'});
        this.setState({appointmentType:data.appointment_type})

    }
    handleCancel=()=>{
        this.setState({visible:false})
        this.setState({date: ''});
        this.setState({availability: ''})
        this.setState({slots: []});
        this.setState({type: ''});
        this.setState({appointmentType:''})
    }
    handleOkEdit=()=>{
        let props = this.props;
        let array = this.state.slots
        array = array.sort(function(a, b){return a-b});
        let data ={
                availability_id: this.state.availability.availability_id,
                doctor_permit_number: this.props.userProfile.permit_number,
                date: this.state.date,
                slots: array,
            }
        console.log(data)
            axios.put('http://127.0.0.1:5000/api/Availability',data ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        props.getAvailabilities();
                        console.log(response.data)
                        this.setState({visible:false})
                        this.setState({date: ''});
                        this.setState({availability: ''})
                        this.setState({slots: []});
                        this.setState({type: ''});
                        this.setState({appointmentType:''})
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
        console.log(this.state.slots)

    }
    updateAvailability=(takenSpots)=>{
        let props = this.props;
        let array = this.state.availability.slots;
            takenSpots.map(pointerData=>{
                if(array.includes(pointerData)){
                    var index = array.indexOf(pointerData);
                    array.splice(index, 1);
                }
                console.log(array)
            })
        if(array.length === 0){
            let data = this.props.availability;

            axios.delete('http://127.0.0.1:5000/api/Availability',{data}).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        props.getAvailabilities();
                         this.setState({visible: false})
                        this.setState({date: ''});
                        this.setState({availability: ''})
                        this.setState({slots: []});
                        this.setState({type: ''});
                        this.setState({appointmentType:''})
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
        }else {

            let data = {
                availability_id: this.state.availability.availability_id,
                doctor_permit_number: this.state.availability.doctor_permit_number,
                date: this.state.date,
                slots: array,
            }
            console.log(data)
            axios.put('http://127.0.0.1:5000/api/Availability', data).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        props.getAvailabilities();
                        console.log(response.data)
                        this.setState({visible: false})
                        this.setState({date: ''});
                        this.setState({availability: ''})
                        this.setState({slots: []});
                        this.setState({type: ''});
                        this.setState({appointmentType:''})
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
        }

    }
    handleOkAdd=()=>{
        let props = this.props;
        let array = this.state.slots
        let this1 = this;
        array = array.sort(function(a, b){return a-b});
        let data ={
                patient_card_number: this.state.cardNumber,
                doctor_permit_number: this.state.availability.doctor_permit_number,
                date: this.state.date,
                slots: array,
                appointment_type: this.state.appointmentType,
            }
            if(this.props.userProfile.type === 'Patient'){
                data.patient_card_number = this.props.userProfile.card_number;
            }
        console.log(data)
            axios.post('http://127.0.0.1:5000/api/Appointment',data ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data)
                        this1.updateAvailability(array);
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    }

    handleOkAdd2=()=>{
        let props = this.props;
        let array = this.state.slots
        let this1 = this;
        array = array.sort(function(a, b){return a-b});
        let data ={
                patient_card_number: this.state.cardNumber,
                doctor_permit_number: this.state.availability.doctor_permit_number,
                date: this.state.date,
                slots: array,
                appointment_type: this.state.appointmentType,
                availability_id:  this.state.availability.availability_id
            }
            if(this.props.userProfile.type === 'Patient'){
                data.patient_card_number = this.props.userProfile.card_number;
            }
        if(!localStorage.getItem('cartAppointments')) {
        var cartAppointments = []
        cartAppointments.push(data)
        localStorage.setItem('cartAppointments', JSON.stringify(cartAppointments))
        }
        else{
            var currentCart = JSON.parse(localStorage.getItem('cartAppointments'));
            console.log(currentCart)
            currentCart.push(data)
            localStorage.setItem('cartAppointments', JSON.stringify(currentCart))
        }
        this.setState({visible: false})
        this.setState({date: ''});
        this.setState({availability: ''})
        this.setState({slots: []});
        this.setState({type: ''});
        this.setState({appointmentType:''})
    }
    changeDate=(e)=>{
        this.setState({date:e.target.value});
    }
    changeSlots=(e, {value})=>{
        if(this.props.userProfile.type !== 'Doctor' && this.state.type === 'add') {
            if(value.length === 0){
                this.setState({slots: value})
            }else if (value.length === 1) {
                this.setState({slots: value})
                if(this.state.appointmentType==='Annual Checkup'){
                    this.setState({submit : true})
                }
            } else if (value.length === 2 && this.state.appointmentType==='Annual Checkup') {
                if (value[0] + 1 === value[1]) {
                    this.setState({slots: value})
                    this.setState({submit : true})
                }
            } else if (value.length === 3 && this.state.appointmentType === 'Annual Checkup') {
                var total = 0;
                var centerValue = value[1];
                value.map(slotsData => {
                    total = total + slotsData;
                })
                if (centerValue === total / 3) {
                    this.setState({slots: value})
                    this.setState({submit : false})
                }
            }
        }else{
            this.setState({slots: value})
        }
    }
    changeCardNumber=(e, {value})=>{
        this.setState({cardNumber:value})

    }
    changeAppointmentType=(e, {value})=>{
        if(this.state.slots.length>=1 && value ==='Walk-In' ){
            let array = [];
            array.push(this.state.slots[0])
            this.setState({slots: array})
        }
        if(this.state.slots.length !== 3 && value ==='Annual Checkup'){
            this.setState({submit : true})
        }else{
            this.setState({submit : false})
        }
        this.setState({appointmentType:value})

    }


    render() {
        if (!this.props.userProfile) {
            return (<Redirect to={'/'}/>);
        } else {
        return (
            <div className="listCal">
                <Modal
                  title={this.state.type === 'add' ? "Add Appointment" : "Edit Availability" }
                  visible={this.state.visible}
                  onOk={this.state.type === 'add' ? (this.props.userProfile.type ==='Patient' ? this.handleOkAdd2 :this.handleOkAdd) : this.handleOkEdit}
                  onCancel={this.handleCancel}
                  okButtonProps={{ disabled: this.state.slots.length > 0 && this.state.date ? (this.state.type === 'add' && this.props.userProfile.type === 'Nurse' && !this.state.cardNumber ? true :
                      this.props.userProfile.type !== 'Doctor' && this.state.type === 'add' && this.state.submit) : true }}
                  okText={'Submit'}
                ><div className='registrationForm-Container-modal'>
                  <Form size='large'  loading={this.state.loading} className='formContainer-modal'>
                <Form.Input
                        icon='calendar times outline'
                        iconPosition='left'
                        placeholder='2019-08-29'
                        label='Availability Date:'
                        type='date'
                        disabled={this.state.type === 'add' ? true : false }
                        value={this.state.date}
                        min={moment(new Date()).format('YYYY-MM-DD')}
                        onChange={this.changeDate}/>
                      {this.state.type === 'add' && this.props.userProfile.type !== 'Doctor' ?
                    <Form.Select
                    search fluid
                    placeholder='ex: KEPE 242141 01'
                    label='Patient Health Card Number:'
                    disabled={this.props.userProfile.type === 'Patient'}
                    value={this.props.userProfile.type === 'Patient' ? this.props.userProfile.card_number : this.state.cardNumber}
                    options={cardOption}
                    onChange={this.changeCardNumber}/>: ''}
                    {this.state.type === 'add' && this.props.userProfile.type !== 'Doctor' ?
                    <Form.Select
                        fluid
                    placeholder='ex: Walk-In (20min)'
                    label='Appointment Type:'
                    value={this.state.appointmentType}
                    options={appointmentTypeOptions}
                    onChange={this.changeAppointmentType}/>:''}
                <Form.Select
                    fluid multiple
                    label='Time Slots'
                    disabled={!this.state.appointmentType && this.props.userProfile.type !== 'Doctor' && this.state.type === 'add'}
                    placeholder='Please Select Time Slot'
                    options={this.state.type === 'add' ? this.state.appointments : appointments}
                    value={this.state.slots}
                    onChange={this.changeSlots}/>
                />
            </Form>
                </div>
                </Modal>
                <div className="cal-box">
                    <div className="cal-list">
                        <div className="cal-date">
                            <div className="cal-date-day">
                                {this.props.availability.date}
                            </div>
                            <div className="cal-date-month">
                            </div>
                        </div>
                        <div className="cal-desc">
                            <div className="cal-title">
                                <span className="cal-title-des"> {this.props.availability.appointment_type}</span>
                                <span lassName="cal-title-time">  Slots : {myConverter.convertArray(this.props.availability.slots).map(slotData=>{
                                    return(<div>{slotData}</div>);
                                })} </span>
                            </div>
                        </div>
                        <div className="PMC-Delete-Edit-buttons">
                            {this.props.userProfile.type === "Doctor"?
                            <div className="note-author" onClick={this.delete}>
                                <Icon name="trash"/> Delete
                            </div>: ''}
                            {this.props.userProfile.type === "Doctor"?
                            <div className="note-author2" onClick={(e)=>this.editAvailability(e,this.props.availability)}>
                                <Icon name="edit"/> Edit
                            </div> : ""}
                            {this.props.userProfile.type !== "Doctor"?
                            <div className="note-author3" onClick={(e)=>this.addAppointment(e,this.props.availability)}>
                                <Icon name="plus"/>Add Appointment
                            </div>: ''}
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