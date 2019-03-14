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

const confirm = Modal.confirm;



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
        let array =[];
        data.slots.map(slotData=>{
            let locationIndex = _.findIndex(appointments, function (o) {
                                        return o.value === slotData;
                                    });
            let arr= {key: appointments[locationIndex].key, value: appointments[locationIndex].value, text: appointments[locationIndex].text}
                            array.push(arr);

        })
        this.setState({appointments: array});
        this.setState({visible:true})
        this.setState({date: data.date});
        this.setState({availability: data})
        this.setState({slots: ''});
        this.setState({type: 'add'});
    }
    editAvailability=(e,data)=>{
        e.preventDefault();
        console.log(data)
        this.setState({visible:true})
        this.setState({date: data.date});
        this.setState({availability: data})
        this.setState({slots: data.slots});
        this.setState({type: 'edit'});
    }
    handleCancel=()=>{
        this.setState({visible:false})
        this.setState({date: ''});
        this.setState({availability: ''})
        this.setState({slots: []});
        this.setState({type: ''});
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
                appointment_type: 'walkin',
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
    changeDate=(e)=>{
        this.setState({date:e.target.value});
    }
    changeSlots=(e, {value})=>{
        this.setState({slots: value})
    }
    changeCardNumber=(e)=>{
        this.setState({cardNumber:e.target.value})

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
                  onOk={this.state.type === 'add' ? this.handleOkAdd : this.handleOkEdit}
                  onCancel={this.handleCancel}
                  okButtonProps={{ disabled: this.state.slots.length > 0 && this.state.date ? (this.state.type === 'add' && this.props.userProfile.type === 'Nurse' && !this.state.cardNumber? true: false) : true }}
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
                      {this.state.type === 'add' && this.props.userProfile.type === 'Nurse' ?
                    <Form.Input
                    icon='address card'
                    iconPosition='left'
                    placeholder='ex: KEPE 242141 01'
                    label='Patient Health Card Number:'
                    value={this.state.cardNumber}
                    onChange={this.changeCardNumber}/>: ''}
                <Form.Select
                    fluid multiple
                    label='Time Slots'
                    placeholder='Please Select Time Slot'
                    options={this.state.type === 'add' ? this.state.appointments : appointments}
                    value={this.state.slots}
                    onChange={this.changeSlots}
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
                                <span lassName="cal-title-time">  Slots : {this.props.availability.slots} </span>
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