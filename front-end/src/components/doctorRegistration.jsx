import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Button, Form, Header} from 'semantic-ui-react'
import axios from "axios";

class DoctorRegistration extends Component {
    constructor(props) {
        super(props);
        this.state = {
            firstName: '',
            lastName: '',
            permitNumber:'',
            location: '',
            specialty:'',
            email: "",
            password: '',
            confirmPassword: '',
            type:'',
            errorFirstName: false,
            errorLastName: false,
            errorPermitNumber:false,
            errorLocation:false,
            errorSpecialty: false,
            errorEmail:false,
            errorPassword:false,
            errorConfirmPassword: false,
            errorType: false,
            loading:false,
        }
    }

    componentDidMount() {

    }

    changeFirstName=(e)=>{
        this.setState({firstName:e.target.value})
        this.setState({errorFirstName: false})
    }
    changeLastName=(e)=>{
        this.setState({lastName:e.target.value})
        this.setState({errorLastName: false})
    }
    changePermitNumber=(e)=>{
        this.setState({permitNumber:e.target.value})
        this.setState({errorPermitNumber: false})

    }
    changeLocation=(e)=>{
        this.setState({location:e.target.value})
        this.setState({errorLocation: false})
    }
    changeSpecialty=(e)=>{
        this.setState({specialty:e.target.value});
        this.setState({errorSpecialty: false})
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
        let {firstName, lastName, permitNumber,location,specialty, email, password,confirmPassword} = this.state;
        if(!firstName || !lastName || !permitNumber || !location || !specialty || !email || !password || !confirmPassword ||  confirmPassword !== password){
            if(!firstName){
                this.setState({errorFirstName: true})
            }
            if(!lastName){
                this.setState({errorLastName: true})
            }
            if(!permitNumber){
                this.setState({errorPermitNumber: true})
            }
            if(!location){
                this.setState({errorLocation: true})
            }
            if(!specialty){
                this.setState({errorSpecialty:false})
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
        }else{
            this.setState({loading:true})
            let data={
                permit_number:permitNumber,
                location:location,
                specialty:specialty,
                email:email,
                password:password,
                last_name: lastName,
                first_name: firstName,
            }
            console.log(data)

            axios.post('http://127.0.0.1:5000/api/Doctor',data).then(
                function (response, err) {
                    console.log(response)
                    if(response.data){
                        console.log(response.data)
                        this.setState({loading:false})
                    }
                }.bind(this)
            ).catch(error=>{
                                  console.log(error)
                });

        }
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
                <Form.Group width='equal'>
                    <Form.Input
                        icon='address card'
                        iconPosition='left'
                        placeholder='ex: 24214101'
                        label='Permit Number:'
                        value={this.state.permitNumber}
                        error={this.state.errorPermitNumber}
                        onChange={this.changePermitNumber}
                        width={8}/>
                    <Form.Input
                        icon='location arrow'
                        iconPosition='left'
                        placeholder='ex: Montreal'
                        label='Location'
                        value={this.state.location}
                        error={this.state.errorLocation}
                        onChange={this.changeLocation}
                        width={8}/>
                </Form.Group>
                <Form.Input
                    fluid icon='user secret'
                    iconPosition='left'
                    placeholder='Ex: Cardiologist'
                    value={this.state.specialty}
                    error={this.state.errorSpecialty}
                    onChange={this.changeSpecialty}
                    label='Specialty:'/>
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
export default withRouter(connect(mapStateToProps)(DoctorRegistration));