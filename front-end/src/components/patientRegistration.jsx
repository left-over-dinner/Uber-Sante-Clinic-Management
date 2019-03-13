import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Button, Form, Header} from 'semantic-ui-react'
import axios from "axios";

class PatientRegistration extends Component {
    constructor(props) {
        super(props);
        this.state = {
            firstName: '',
            lastName: '',
            cardNumber:'',
            birthDay: '',
            gender:'',
            phone:'',
            address:'',
            email: "",
            password: '',
            confirmPassword: '',
            type:'',
            errorFirstName: false,
            errorLastName: false,
            errorCardNumber:false,
            errorBirthDay:false,
            errorGender: false,
            errorPhone: false,
            errorAddress: false,
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
        let {firstName, lastName, cardNumber,birthDay,address,phone, email, password,confirmPassword,gender} = this.state;
        if(!firstName || !lastName || !cardNumber || !birthDay || !address || !phone || !gender|| !email || !password || !confirmPassword ||  confirmPassword !== password){
            if(!firstName){
                this.setState({errorFirstName: true})
            }
            if(!lastName){
                this.setState({errorLastName: true})
            }
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
            let data={
                card_number:cardNumber,
                birth_day:birthDay,
                gender:gender,
                phone_number:phone,
                address:address,
                email:email,
                password:password,
                last_name: lastName,
                first_name: firstName,
            }

            axios.post('http://127.0.0.1:5000/api/Patient',data).then(
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
            </Form>)
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(PatientRegistration));