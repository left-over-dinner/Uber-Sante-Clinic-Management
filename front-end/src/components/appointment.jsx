import React, {Component, Fragment} from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Icon, Form} from 'semantic-ui-react'
import '../appointment.css'
import axios from "axios";
import {Redirect} from "react-router";
import {TimeSlotConverter} from "./calculator";
import {Modal} from "antd";
import moment from "moment";
import {appointments} from "./options";
import _ from "lodash";

const myConverter = new TimeSlotConverter();
const confirm = Modal.confirm;

var appointmentTypeOptions = [
    {key: 1, value: 'Walk-In', text: 'Walk-In (20min)'},
    {key: 2, value: 'Annual Checkup', text: "Annual Checkup (60min)"}];
class Appointment extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: false,
            slots: [],
            appointmentType: '',
            appointments: [],
            date: '',
            visible: false,
            availability: '',
            submit: false,
            appointment: '',
        }
    }


    componentDidMount() {

    }
    handleCancel=()=>{
        this.setState({visible:false})
        this.setState({date: ''});
        this.setState({availability: ''})
        this.setState({slots: []});
        this.setState({appointmentType:''})
        this.setState({appointments:[]})
        this.setState({appointment:''})

    }
    delete=()=>{
        let this1 = this;
        let props = this.props;
        let data = this.props.appointments;
        let availabilities = this.props.availabilities;
        console.log(data)
        confirm({
    title: 'Are you sure to delete this appointment?',
    content: 'Note that this operation will delete permanently.',
    okText: 'Delete',
    okType: 'danger',
    cancelText: 'Cancel',
    onOk() {
        console.log(data)
        axios.delete('http://127.0.0.1:5000/api/Appointment',{data} ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        let pointer =false;
                        availabilities.map(availabilityData=>{
                            if(availabilityData.doctor_permit_number === data.doctor_permit_number && availabilityData.date === data.date){
                                pointer = availabilityData;
                            }
                        })
                        if(pointer){
                            this1.updateAvailability(pointer,data);
                        }else{
                            this1.addAvailability(data);
                        }

                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    },
  });
    }
    editAppointment=(e,data)=>{
        e.preventDefault();
        console.log(data)
        var this1= this;
        let availability = '';
        let array =[];
        var availabilities = this.props.availabilities;
        data.slots.map(slotData=>{
                    let locationIndex = _.findIndex(appointments, function (o) {
                    return o.value === slotData;
                });
                    let arr = {
                    key: appointments[locationIndex].key,
                    value: appointments[locationIndex].value,
                    text: appointments[locationIndex].text
                }
                array.push(arr);
                })
                console.log(array)
        availabilities.map(availabilityData=>{
            if(availabilityData.doctor_permit_number === data.doctor_permit_number && availabilityData.date ===data.date){
                availability = availabilityData;

            }
        })
        if(availability) {
            availability.slots.map(slotData => {
                let locationIndex = _.findIndex(appointments, function (o) {
                    return o.value === slotData;
                });
                let arr = {
                    key: appointments[locationIndex].key,
                    value: appointments[locationIndex].value,
                    text: appointments[locationIndex].text
                }
                array.push(arr);

            })
        }
        array = array.sort(function(a, b){return a.key-b.key});
        this.setState({appointments:array})
        this.setState({date: data.date});
        this.setState({availability: availability})
        this.setState({slots: data.slots});
        this.setState({appointmentType: data.appointment_type})
        this.setState({visible:true})
        this.setState({appointment:data})
    }

    updateAvailability=(pointer,appointmentData)=> {
        let props = this.props;
        let array = pointer.slots;
        appointmentData.slots.map(slotData=>{
            array.push(slotData)
        })

        array = array.sort(function (a, b) {
            return a - b
        });
        console.log(array)
        let data = {
            availability_id: pointer.availability_id,
            doctor_permit_number: pointer.doctor_permit_number,
            date: pointer.date,
            slots: array,
        }
        console.log(data)
        axios.put('http://127.0.0.1:5000/api/Availability', data).then(
            function (response, err) {
                console.log(response)
                if (response.data) {
                    props.getAvailabilities();

                }
            }.bind(this)
        ).catch(error => {
            console.log(error)
        });
    }
    updateAvailability2=(availabilityData)=> {
        let props = this.props;
        let array=[]
        let availabilityArray = availabilityData.slots;
        let appointmentData = this.state.appointment;
        appointmentData.slots.map(appointments=>{
            availabilityArray.push(appointments)
        })
        availabilityArray = availabilityArray.sort(function (a, b) {
            return a - b
        });
        availabilityArray.map(oldSlotData=>{
            var pointer=false
            this.state.slots.map(newSlotData=>{
                if(oldSlotData === newSlotData){
                    pointer = true;
                }
            })
            if(!pointer){
                array.push(oldSlotData)
                console.log(array)
            }
        })
        array = array.sort(function (a, b) {
            return a - b
        });
        array = _.sortedUniq(array)
        console.log(array)
        if(array.length ===0){
            let data = {
                availability_id: availabilityData.availability_id,
                doctor_permit_number: availabilityData.doctor_permit_number,
                date: availabilityData.date,
                slots: array,
            }
            console.log(data)
            axios.delete('http://127.0.0.1:5000/api/Availability', {data}).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        props.getAvailabilities();

                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });

        }else {
            let data = {
                availability_id: availabilityData.availability_id,
                doctor_permit_number: availabilityData.doctor_permit_number,
                date: availabilityData.date,
                slots: array,
            }
            console.log(data)
            axios.put('http://127.0.0.1:5000/api/Availability', data).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        props.getAvailabilities();

                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
        }
    }
    addAvailability(appointmentData){
        let props = this.props;
            let data ={
                doctor_permit_number: appointmentData.doctor_permit_number,
                date: appointmentData.date,
                slots: appointmentData.slots,
            }
        console.log(data)
            axios.post('http://127.0.0.1:5000/api/Availability',data ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        props.getAvailabilities();
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    }
    addAvailability2(appointmentData){
        let props = this.props;
        let array=[]
        appointmentData.slots.map(oldSlotData=>{
            var pointer=false
            this.state.slots.map(newSlotData=>{
                if(oldSlotData === newSlotData){
                    pointer = true;
                }
            })
            if(!pointer){
                array.push(oldSlotData)
            }

        })
        array = _.sortedUniq(array)
            let data ={
                doctor_permit_number: appointmentData.doctor_permit_number,
                date: appointmentData.date,
                slots: array,
            }
        console.log(data)
            axios.post('http://127.0.0.1:5000/api/Availability',data ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        props.getAvailabilities();
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    }

    handleOkAdd=()=>{
        let props = this.props;
        let array = this.state.slots
        let this1 = this;
        array = array.sort(function(a, b){return a-b});
        let data ={
                patient_card_number: this.state.appointment.patient_card_number,
                doctor_permit_number: this.state.appointment.doctor_permit_number,
                date: this.state.date,
                slots: array,
                appointment_type: this.state.appointmentType,
            }
        console.log(data)
            axios.put('http://127.0.0.1:5000/api/Appointment',data ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data)
                        if(this.state.availability){
                            this1.updateAvailability2(this.state.availability)
                        }else{
                            this1.addAvailability2(this.state.appointment)
                        }
                        this.setState({visible:false})
                        this.setState({date: ''});
                        this.setState({availability: ''})
                        this.setState({slots: []});
                        this.setState({appointmentType:''})
                        this.setState({appointments:[]})
                        this.setState({appointment:''})
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    }

    changeSlots=(e, {value})=>{
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
                  title={"Edit Appointment"}
                  visible={this.state.visible}
                  onOk={this.handleOkAdd}
                  onCancel={this.handleCancel}
                  okButtonProps={{ disabled: this.state.slots.length === 0 || !this.state.date || this.state.submit }}
                  okText={'Submit'}
                ><div className='registrationForm-Container-modal'>
                  <Form size='large'  loading={this.state.loading} className='formContainer-modal'>
                <Form.Input
                        icon='calendar times outline'
                        iconPosition='left'
                        placeholder='2019-08-29'
                        label='Availability Date:'
                        type='date'
                        disabled={true}
                        value={this.state.date}/>
                    <Form.Select
                        fluid
                    placeholder='ex: Walk-In (20min)'
                    label='Appointment Type:'
                    value={this.state.appointmentType}
                    options={appointmentTypeOptions}
                    onChange={this.changeAppointmentType}/>
                <Form.Select
                    fluid multiple
                    label='Time Slots'
                    disabled={!this.state.appointmentType}
                    placeholder='Please Select Time Slot'
                    options={this.state.appointments}
                    value={this.state.slots}
                    onChange={this.changeSlots}/>
            </Form>
                </div>
                </Modal>
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
                                })}</span>
                            </div>
                             {this.props.userProfile.type === "Patient"?
                            <span className="cal-title-time"> Clinic : {this.props.appointments.clinicName} <br/> </span>: null}
                            {this.props.userProfile.type === "Patient"? null :
                            <span className="cal-title-time"> Patient : {this.props.appointments.patientFirstName} {this.props.appointments.patientLastName} <br/> </span>}
                            {this.props.userProfile.type === "Patient"? null :
                            <span className="cal-title-time"> Patient Card Number : {this.props.appointments.patient_card_number} <br/></span>}
                            {this.props.userProfile.type === "Nurse"?
                            <span className="cal-title-time"> Doctor : {this.props.appointments.doctorFirstName} {this.props.appointments.doctorLastName}  <br/></span> : null}
                            {this.props.userProfile.type === "Doctor"? null :
                            <span className="cal-title-time"> Doctor Speciality : {this.props.appointments.doctorSpeciality} <br/></span>}
                            {this.props.userProfile.type === "Nurse"?
                            <span className="cal-title-time"> Doctor Permit Number : {this.props.appointments.doctor_permit_number} <br/></span> : null}
                        </div>
                        <div className="PMC-Delete-Edit-buttons">
                            {this.props.userProfile.type !== "Doctor"?
                            <div className="note-author" onClick={this.delete}>
                                <Icon name="trash"/> Delete
                            </div> : null }
                            {this.props.userProfile.type !== "Doctor"?
                            <div className="note-author2" onClick={(e)=>this.editAppointment(e,this.props.appointments)}>
                                <Icon name="edit"/> Edit
                            </div> : null}
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