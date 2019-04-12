import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Tab, Loader, Button, Header, Form, Select} from 'semantic-ui-react'
import Availability from './availibility'
import axios from "axios";
import {CalculateAvailability} from './calculator.jsx'
import { Modal } from 'antd';
import {availableFrom,availableTo} from "./options";
import moment from 'moment'
import {Redirect} from "react-router";
import DoctorRegistration from "./registrationForm";
import DataIterator from "./iterator";


let Doctors=[];
let Clinics=[];
let DoctorsArray=[]
class Appointments extends Component {
    constructor(props) {
        super(props);
        this.state = {
            availabilities:[],
            loading:false,
            visible:false,
            date:'',
            availableFrom: '',
            availableTo: '',
            doctorPermit: '',
        }
    }

    componentDidMount() {
        if (this.props.userProfile.type ==='Doctor') {
            this.getAvailabilitiesDoctor();
        }else{
            this.setState({loading: true})
            Doctors=[];
            axios.get('http://127.0.0.1:5000/api/Doctor').then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        response.data.data.map(doctorData=>{
                            Doctors.push(doctorData);
                        })
                        console.log(Doctors)
                        var this1 = this;
                        setTimeout(function(){  this1.setState({loading: false}) }, 1000);
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
            Clinics=[];
            axios.get('http://127.0.0.1:5000/api/Clinics').then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        response.data.data.map(clinicData=>{
                            if(clinicData.no_doctors === 7) {
                                console.log(clinicData)
                                let arr = {
                                    key: clinicData.clinic_id,
                                    value: clinicData.clinic_id,
                                    text: clinicData.name
                                }
                                Clinics.push(arr);
                            }
                        })
                        console.log(Clinics)
                         var this1 = this;
                        if(this1.props.userProfile.type !== 'Patient'){
                            this1.setState({clinic_id: this1.props.userProfile.clinic_id})
                            this1.filterDoctors(this1.props.userProfile.clinic_id)
                        }
                        setTimeout(function(){  this1.setState({loading: false}) }, 1000);
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
        }
    }
    getAvailabilitiesforDoctor=(doctorPermit)=>{
        this.setState({loading: true})
        axios.get('http://127.0.0.1:5000/api/Availability').then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        let array =[];
                            response.data.data.map(data=>{
                            if(data.doctor_permit_number ===  doctorPermit){
                                array.push(data);
                            }
                        });
                            array = array.sort(function compare(a, b) {
                                var dateA = moment(a.date || "YYYY-MM-DD HH:mm");
                                var dateB = moment(b.date || "YYYY-MM-DD HH:mm");
                                return dateA - dateB;
                            });
                            console.log(array)
                        this.setState({doctorPermit: doctorPermit})
                        this.setState({availabilities: array})
                        var this1 = this;
                        setTimeout(function(){  this1.setState({loading: false}) }, 1000);
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    }
    getAvailabilitiesDoctor=()=>{
        this.setState({loading: true})
            axios.get('http://127.0.0.1:5000/api/Availability').then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        let array =[];
                            response.data.data.map(data=>{
                            if(data.doctor_permit_number ===  this.props.userProfile.permit_number){
                                array.push(data);
                            }
                        });
                            array = array.sort(function compare(a, b) {
                                var dateA = moment(a.date || "YYYY-MM-DD HH:mm");
                                var dateB = moment(b.date || "YYYY-MM-DD HH:mm");
                                return dateA - dateB;
                            });
                            console.log(array)
                        this.setState({doctorPermit: this.props.userProfile.permit_number})
                        this.setState({availabilities: array})
                        var this1 = this;
                        setTimeout(function(){  this1.setState({loading: false}) }, 1000);
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });

    }

    addAvailability=()=>{
        this.setState({visible:true})
        this.setState({date: ''});
        this.setState({availableFrom: ''})
        this.setState({availableTo: ''})
    }
    handleCancel=()=>{
        this.setState({visible:false})
        this.setState({date: ''});
        this.setState({availableFrom: ''})
        this.setState({availableTo: ''})
    }
    handleOk=()=>{
        let pointer =false;
        this.state.availabilities.map(availabilityData=>{
            console.log(availabilityData.date)
                console.log(this.state.date)
            if(availabilityData.date === this.state.date){
                pointer = availabilityData;
            }
        });
        if(pointer){
             let array =[];
            for(var i =this.state.availableFrom;i <= this.state.availableTo; i++){
                array.push(i)
            }
            pointer.slots.map(pointerData=>{
                if(!array.includes(pointerData)){
                    array.push(pointerData)
            }
            })
            array = array.sort(function(a, b){return a-b});
            console.log(array)
            let data ={
                availability_id: pointer.availability_id,
                doctor_permit_number: this.props.userProfile.permit_number,
                date: this.state.date,
                slots: array,
            }
        console.log(data)
            axios.put('http://127.0.0.1:5000/api/Availability',data ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        this.getAvailabilitiesDoctor();
                        console.log(response.data)
                        this.setState({visible:false})
                        this.setState({date: ''});
                        this.setState({availableFrom: ''})
                        this.setState({availableTo: ''})
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
        }else{
            let array =[];
            for(var i =this.state.availableFrom;i <= this.state.availableTo; i++){
                array.push(i)
            }
            let data ={
                doctor_permit_number: this.props.userProfile.permit_number,
                date: this.state.date,
                slots: array,
            }
        console.log(data)
            axios.post('http://127.0.0.1:5000/api/Availability',data ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        this.getAvailabilitiesDoctor();
                        console.log(response.data)
                        this.setState({visible:false})
                        this.setState({date: ''});
                        this.setState({availableFrom: ''})
                        this.setState({availableTo: ''})
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
        }
    }
    changeDate=(e)=>{
        this.setState({date:e.target.value});
        if(moment(e.target.value).format("YY-MM-DD") < moment(new Date).format("YY-MM-DD")){
        this.setState({date: ''});
        }
    }
    changeAvailableFrom=(e, {value,text})=>{
        this.setState({availableFrom: value})
    }
    changeAvailableTo=(e, {value})=>{
        this.setState({availableTo: value})
    }

    filterDoctors=(clinicID)=>{
        DoctorsArray=[];
        let Iterator =  new DataIterator(Doctors);
        while(Iterator.hasNext()){
            let doctor = Iterator.next()
            if(doctor.clinic_id===clinicID){
                console.log(doctor)
                let arr= {key: doctor.permit_number, value: doctor.permit_number, text: doctor.specialty}
                DoctorsArray.push(arr)
            }

        }


    }

    changeClinic=(e, {value})=>{
        console.log(value)
        this.setState({clinic_id: value})
        this.filterDoctors(value);
    }

    changeDoctor=(e, {value})=>{
        this.setState({doctorPermit: value})
        if(value){
            this.getAvailabilitiesforDoctor(value);
        }
    }


    render() {
        if(!this.props.userProfile){
            return (<Redirect to={'/login'}/>);
        }else if(this.state.loading){
            return(
                <div className='registrationForm-Container'>
                    <div className='loader-container'>
                <Loader active  inline='centered' />
                    </div>
                </div>)
        }else if(!this.state.doctorPermit) {
            return (<div className='registrationForm-Container'>
                <div className="registrationForm-Container-upper-container">
                    <div className="registrationForm-Container-upper-container-text">
                        <div className="registrationForm-Container-upper-container-first-text">
                            Selecting Clinic and Speciality
                        </div>
                        <div className="registrationForm-Container-upper-container-second-text">
                       Please first choose the clinic and then the Speciality to see availabilities

                        </div>
                    </div>
                </div>
                    <Form size='large' loading={this.state.loading} className='formContainer-modal'>
                        <Header as='h2' style={{marginTop: '3%', fontFamily: 'Fahkwang'}} textAlign='center'>
                            Choose Clinic & Speciality
                        </Header>
                        <Form.Select
                            fluid
                            placeholder='Please Select A Option'
                            options={Clinics}
                            value={this.state.clinic_id}
                            disabled={this.props.userProfile.type !== 'Patient'}
                            onChange={this.changeClinic}
                        />
                        <Form.Select
                            fluid
                            placeholder='Please Select A Option'
                            options={DoctorsArray}
                            disabled={!this.state.clinic_id}
                            value={this.state.doctorPermit}
                            onChange={this.changeDoctor}
                        />
                    </Form>
            </div>)
        }else {
            return (<div className='registrationForm-Container'>
                {this.props.userProfile.type === "Doctor"?
                <Button size='small' onClick={this.addAvailability}>
                        Add Availability
                    </Button>:
                    <div className='dropdown-flex'>
                    <Form.Select
                            fluid
                            placeholder='Please Select A Option'
                            options={Clinics}
                            value={this.state.clinic_id}
                            disabled={this.props.userProfile.type !== 'Patient'}
                            onChange={this.changeClinic}
                        />
                    <Form.Select
                            style={{marginLeft:'5%'}}
                            placeholder='Please Select A Option'
                            options={DoctorsArray}
                            value={this.state.doctorPermit}
                            onChange={this.changeDoctor}
                        /></div>}
                <Modal
                  title="Add Availability"
                  visible={this.state.visible}
                  onOk={this.handleOk}
                  onCancel={this.handleCancel}
                  okButtonProps={{ disabled: this.state.availableFrom && this.state.availableTo && this.state.date ? false : true }}
                  okText={'Submit'}
                ><div className='registrationForm-Container-modal'>
                  <Form size='large'  loading={this.state.loading} className='formContainer-modal'>
                <Form.Input
                        icon='calendar times outline'
                        iconPosition='left'
                        placeholder='2019-08-29'
                        label='Availability Date:'
                        type='date'
                        value={this.state.date}
                        min={moment(new Date()).format('YYYY-MM-DD')}
                        onChange={this.changeDate}/>
                <Form.Select
                    fluid
                    label='Available From:'
                    placeholder='Please Select Time Slot'
                    options={availableFrom}
                    value={this.state.availableFrom}
                    onChange={this.changeAvailableFrom}
                />
                <Form.Select
                    fluid
                    label='Available To:'
                    placeholder='Please Select Time Slot'
                    options={availableTo}
                    value={this.state.availableTo}
                    onChange={this.changeAvailableTo}
                />
            </Form>
                </div>
                </Modal>
                <Tab className='appointment-tab' menu={{secondary: true, pointing: true}} panes={
                    [
                        {
                            menuItem: "Availabilities" + " (" + this.state.availabilities.length + ")",
                            render: () =>
                                <Tab.Pane attached={false}>
                                    {this.state.availabilities.map(availabilityData => {
                                        return (<Availability getAvailabilities={this.getAvailabilitiesDoctor} availability={availabilityData}/>);
                                    })}
                                </Tab.Pane>
                        },
                        /*{
                            menuItem: nextweek,
                            render: () =>
                                <Tab.Pane attached={false}>
                                    <Appointment/>
                                </Tab.Pane>
                        },
                        {
                            menuItem: thismonth,
                            render: () =>
                                <Tab.Pane attached={false}>
                                    <Appointment/>
                                </Tab.Pane>
                        },
                        {
                            menuItem: nextmonths,
                            render: () =>
                                <Tab.Pane attached={false}>
                                    <Appointment/>
                                </Tab.Pane>
                        },
                        {
                            menuItem: pastevents,
                            render: () =>
                                <Tab.Pane attached={false}>
                                    <Appointment/>
                                </Tab.Pane>
                        },*/

                    ]
                }/>
            </div>)
        }
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(Appointments));