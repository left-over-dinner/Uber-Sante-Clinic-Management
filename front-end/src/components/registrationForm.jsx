import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Button, Form, Header} from 'semantic-ui-react'
import axios from "axios";

const gender = [
    {key: 'Male', value: 'Male', text: 'Male'},
    {key: 'Female', value: 'Female', text: 'Female'}
]
class RegistrationForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            cardNumber:'',
            birthDay: '',
            gender:'',
            phone:'',
            address:'',
            email: "",
            password: '',
            confirmPassword: '',
            errorCardNumber:'',
            errorBirthDay:'',
            errorGender: false,
            errorPhone: false,
            errorAddress: false,
            errorEmail:false,
            errorPassword:false,
            errorConfirmPassword: false,
            loading:false,
        }
    }

    componentDidMount() {

    }
    changeCardNumber=(e)=>{
        this.setState({cardNumber:e.target.value})
        this.setState({errorCardNumber: false})

    }
    changeBirthdate=(e)=>{
        this.setState({birthDay:e.target.value})
        this.setState({errorBirthDay: false})
    }
    changeGender=(e)=>{
        this.setState({gender:e.target.value});
        this.setState({errorGender: false})
    }
    changePhone=(e)=>{
        this.setState({phone:e.target.value});
        this.setState({errorPhone: false})
    }
    changeAddress=(e)=>{
        this.setState({address:e.target.value});
        this.setState({errorAddress: false})
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
        let {cardNumber,birthDay,address,phone, email, password,confirmPassword,gender} = this.state;
        if(!cardNumber || !birthDay || !address || !phone || !gender|| !email || !password || !confirmPassword ||  confirmPassword !== password){
            if(!cardNumber){
                this.setState({errorCardNumber: true})
            }
            if(!birthDay){
                this.setState({errorBirthDay: true})
            }
            if(!gender){
                this.setState({errorGender:false})
            }
            if(!address){
                this.setState({errorAddress: true})
            }
            if(!phone){
                this.setState({errorPhone:true})
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

        }
    }
    chatroom=()=>{
        var data ={
            email:'erdem@gmail.com',
            name: 'erdem'

        }
        console.log(data)
        axios.post('/session/auth',{data:data}).then(
            function (response, err) {
                console.log(response)
                if(response.data){
                    console.log(data)
                }
            }.bind(this)
        );
    }

    render() {
        return (<div className='registrationForm-Container'>
            <div className="registrationForm-Container-upper-container">
                <div className="registrationForm-Container-upper-container-text">
                    <div className="registrationForm-Container-upper-container-first-text">
                        Registration
                    </div>
                    <div className="registrationForm-Container-upper-container-second-text">
                        Please enter your personal information

                    </div>
                </div>
            </div>
            <Form size='large'  loading={this.state.loading} className='formContainer'>
                <Header as='h2'  style={{marginTop:'3%', fontFamily: 'Fahkwang'}}textAlign='center'>
                    Profile Information
                </Header>
                <Form.Group width='equal'>
                    <Form.Input
                        icon='address card'
                        iconPosition='left'
                        placeholder='ex: KEPE 242141 01'
                        label='Health Card Number:'
                        value={this.state.cardNumber}
                        error={this.state.errorCardNumber}
                        onChange={this.changeCardNumber}
                        width={8}/>
                    <Form.Input
                        icon='birthday'
                        iconPosition='left'
                        placeholder='1992-05-13'
                        label='Date of Birth:'
                        type='date'
                        value={this.state.birthDay}
                        error={this.state.errorBirthDay}
                        onChange={this.changeBirthdate}
                        width={8}/>
                </Form.Group>
                <Form.Group width='equal'>
                <Form.Input
                    icon='transgender'
                    iconPosition='left'
                    placeholder='Ex: Male'
                    label='Gender:'
                    value={this.state.gender}
                    error={this.state.errorGender}
                    onChange={this.changeGender}
                    width={8}/>
                    <Form.Input
                        icon='phone'
                        iconPosition='left'
                        label='Phone:'
                        placeholder='Ex: 514 232 9332'
                        type='number'
                        value={this.state.phone}
                        error={this.state.errorPhone}
                        onChange={this.changePhone}
                        width={8}/>
                </Form.Group>
                <Form.Input
                    fluid icon='address book'
                    iconPosition='left'
                    placeholder='1200 Rue Guy #201'
                    value={this.state.address}
                    error={this.state.errorAddress}
                    onChange={this.changeAddress}
                    label='Address:'/>
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
            </Form>
        </div>)
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(RegistrationForm));