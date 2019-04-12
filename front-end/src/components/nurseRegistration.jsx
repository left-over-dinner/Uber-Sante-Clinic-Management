import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Button, Form, Header} from 'semantic-ui-react'
import axios from "axios";

var Clinics=[];
var Nurses=[];

class NurseRegistration extends Component {
    constructor(props) {
        super(props);
        this.state = {
            firstName: '',
            lastName: '',
            accessId:'',
            email: "",
            password: '',
            confirmPassword: '',
            type:'',
            errorFirstName: false,
            errorLastName: false,
            errorAccessId:false,
            errorEmail:false,
            errorPassword:false,
            errorConfirmPassword: false,
            errorClinicID:false,
            errorType: false,
            loading:false,
            clinic_id: '',
        }
    }

    componentDidMount() {
        Nurses=[];
            axios.get('http://127.0.0.1:5000/api/Nurse').then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                        response.data.data.map(nurseData=>{
                            Nurses.push(nurseData);
                        })
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
                            console.log(clinicData)
                            let arr= {key: clinicData.clinic_id, value: clinicData.clinic_id, text: clinicData.name}
                            Clinics.push(arr);
                        })
                        console.log(Clinics)
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });

    }

    changeFirstName=(e)=>{
        this.setState({firstName:e.target.value})
        this.setState({errorFirstName: false})
    }
    changeLastName=(e)=>{
        this.setState({lastName:e.target.value})
        this.setState({errorLastName: false})
    }
    changeAccessId=(e)=>{
        this.setState({accessId:e.target.value})
        this.setState({errorAccessId: false})

    }
    changeEmail=(e)=>{
        this.setState({email:e.target.value})
        this.setState({errorEmail: false})
    }
    changePassword=(e)=>{
        this.setState({password:e.target.value})
        this.setState({errorPassword: false})
    }
    changeConfirmPassword=(e)=>{
        this.setState({confirmPassword:e.target.value})
        this.setState({errorConfirmPassword: false})
    }
    register=()=>{
        let {firstName, lastName, accessId, email, password,confirmPassword, clinic_id} = this.state;
        if(!firstName || !lastName || !accessId  || !email || !password || !confirmPassword ||  confirmPassword !== password || !clinic_id){
            if(!firstName){
                this.setState({errorFirstName: true})
            }
            if(!lastName){
                this.setState({errorLastName: true})
            }
            if(!accessId){
                this.setState({errorAccessId: true})
            }
            if(!email){
                this.setState({errorEmail: true})
            }
            if(!password){
                this.setState({errorPassword: true})
            }
            if(!confirmPassword){
                this.setState({errorConfirmPassword: true})
            }
            if(confirmPassword !== password ){
                this.setState({errorPassword: true})
                this.setState({errorConfirmPassword: true})
            }
            if(!clinic_id){
                this.setState({errorClinicID: true})
            }
        }else{
            this.setState({loading:true})
            let data={
                access_id:accessId,
                email:email,
                password:password,
                last_name: lastName,
                first_name: firstName,
                clinic_id: clinic_id
            }

            axios.post('http://127.0.0.1:5000/api/Nurse',data).then(
                function (response, err) {
                    console.log(response)
                    if(response.data){
                        this.setState({loading:false})
                    }
                }.bind(this)
            ).catch(error=>{
                                  console.log(error)
                });

        }
    }

    changeClinic=(e, {value})=>{
        this.setState({clinic_id: value})
    }

    render() {
        return(<Form size='large'  loading={this.state.loading} className='formContainer'>
                <Header as='h2'  style={{marginTop:'3%', fontFamily: 'Fahkwang'}}textAlign='center'>
                    Profile Information
                </Header>
                <Form.Group width='equal'>
                    <Form.Input
                        icon='user'
                        iconPosition='left'
                        placeholder='ex: John'
                        label='First Name:'
                        value={this.state.firstName}
                        error={this.state.errorFirstName}
                        onChange={this.changeFirstName}
                        width={8}/>
                    <Form.Input
                        icon='user outline'
                        iconPosition='left'
                        placeholder='Dylon'
                        label='Last Name:'
                        value={this.state.lastName}
                        error={this.state.errorLastName}
                        onChange={this.changeLastName}
                        width={8}/>
                </Form.Group>
                <Form.Input
                    icon='address card'
                    iconPosition='left'
                    placeholder='ex: 24294294'
                    label='Access Id:'
                    value={this.state.accessId}
                    error={this.state.errorAccessId}
                    onChange={this.changeAccessId}/>
                <Form.Input
                    fluid icon='mail'
                    iconPosition='left'
                    placeholder='john@concordia.ca'
                    value={this.state.email}
                    error={this.state.errorEmail}
                    onChange={this.changeEmail}
                    label='Email:'/>
                <Form.Input
                    fluid
                    icon='lock'
                    iconPosition='left'
                    label='Password'
                    placeholder='Password'
                    type='password'
                    value={this.state.password}
                    error={this.state.errorPassword}
                    onChange={this.changePassword}
                />
                <Form.Input
                    fluid
                    icon='lock'
                    iconPosition='left'
                    label='Confirm Password'
                    placeholder='Password'
                    type='password'
                    value={this.state.confirmPassword}
                    error={this.state.errorConfirmPassword}
                    onChange={this.changeConfirmPassword}
                />
                <Form.Select
                            label='Select Clinic'
                            placeholder='Please Select A Option'
                            options={Clinics}
                            error={this.state.errorClinicID}
                            value={this.state.clinic_id}
                            onChange={this.changeClinic}
                        />
                <Button className='david'  fluid size='large' style={{marginTop: '5%'}} onClick={this.register}>
                    Submit
                </Button>
            </Form>)
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(NurseRegistration));