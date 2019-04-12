import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Loader, Tab} from 'semantic-ui-react'
import Appointment from './appointment'
import axios from "axios";

class Appointments extends Component {
    constructor(props) {
        super(props);
        this.state = {
            appointments: [],
            loading:false,
            availabilities: [],
        }
    }

    componentDidMount() {
        if (this.props.userProfile) {
            this.setState({loading: true})
            this.getAvailabilities();
        }
    }
    getAppointments=()=>{
        let data = {
                email: this.props.userProfile.email
            }
            axios.get('http://127.0.0.1:5000/api/Appointment', data).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        let array =[];
                        if(this.props.userProfile.type ==='Doctor'){
                            response.data.data.map(data=>{
                            if(data.doctor_permit_number ===  this.props.userProfile.permit_number){
                                array.push(data);
                            }
                        });
                        this.setState({appointments: array})
                        }else if(this.props.userProfile.type === 'Patient'){
                          response.data.data.map(data=>{
                            if(data.patient_card_number ===  this.props.userProfile.card_number){
                                array.push(data);
                            }
                        });
                        this.setState({appointments: array})
                        }else{
                            response.data.data.map(data=>{
                            if(data.clinic_id ===  this.props.userProfile.clinic_id){
                                array.push(data);
                            }
                        });
                        this.setState({appointments: array})
                        }
                        console.log(array)
                        var this1 = this;
                         setTimeout(function(){  this1.setState({loading: false}) }, 1000);
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
            console.log('Retrieved data for Appointment.')

    }

    getAvailabilities=()=>{
        axios.get('http://127.0.0.1:5000/api/Availability').then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        this.setState({availabilities: response.data.data})
                        this.getAppointments();
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    }


    render() {
         if(this.state.loading){
            return(
                <div className='registrationForm-Container'>
                    <div className='loader-container'>
                <Loader active  inline='centered' />
                    </div>
                </div>)
        }else {
             return (<div className='registrationForm-Container'>
                 <Tab className='appointment-tab' menu={{secondary: true, pointing: true}} panes={
                     [
                         {
                             menuItem: "Appointments" + " (" + this.state.appointments.length + ")",
                             render: () =>
                                 <Tab.Pane attached={false}>
                                     {this.state.appointments.map(appointmentData => {
                                         return (<Appointment availabilities={this.state.availabilities} getAvailabilities={this.getAvailabilities} getAppointments={this.getAppointments} appointments={appointmentData}/>);
                                     })}
                                 </Tab.Pane>
                         },


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