import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Button, Form, Header} from 'semantic-ui-react'
import {Redirect} from "react-router";
import axios from "axios";

const types = [
    {key: 'Doctor', value: 'Doctor', text: 'Doctor'},
    {key: 'Patient', value: 'Patient', text: 'Patient'},
    {key: 'Nurse', value: 'Nurse', text: 'Nurse'}
]
class RegistrationForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            email: "",
            password: '',
            type:'',
            errorEmail:false,
            errorPassword:false,
            errorType:false,
            loading:false
        }
    }

    componentDidMount() {

    }
    changeEmail=(e)=>{
        this.setState({email:e.target.value})
        this.setState({errorEmail: false})
    }
    changePassword=(e)=>{
        this.setState({password:e.target.value})
        this.setState({errorPassword: false})
    }
    changeType=(e, {value})=>{
        this.setState({type: value})
        this.setState({errorType: false})
    }

    login=()=> {
        let { email, password, type} = this.state;
        console.log("hello")
        if (!email || !password || !type) {
            if (!email) {
                this.setState({errorEmail: true})
            }
            if (!password) {
                this.setState({errorPassword: true})
            }
            if (!type) {
                this.setState({errorType: true})
            }
        } else {

            this.setState({loading: true})
            let data={
                email:email,
                password:password,
                type:type
            }
            console.log(data)
            axios.post('http://127.0.0.1:5000/api/Login',data).then(
                function (response, err) {
                    console.log("message received")
                    console.log(response)
                    if(response.data.status === 'success'){
                        let jwtData = response.data.data
                        jwtData.type = type;
                        this.setState({loading:false})
                        localStorage.setItem('jwtToken', JSON.stringify(jwtData));
                        this.props.dispatch({type: 'addUserProfile', data: jwtData});
                        this.props.dispatch({type: 'activeMenuItem', data: "Appointments"});

                    }
                    else if(response.data.message=== 'Invalid Login'){
                        this.setState({loading:false})
                    }else{
                        this.setState({loading:false})
                    }
                }.bind(this)
            ).catch(error=>{
                                  console.log(error)
                });
        }
    }
    render() {
        if(this.props.userProfile){
            return (<Redirect to={'/appointments'}/>);
        }else {
            return (<div className='registrationForm-Container'>
                <div className="registrationForm-Container-upper-container">
                    <div className="registrationForm-Container-upper-container-text">
                        <div className="registrationForm-Container-upper-container-first-text">
                            Signing In
                        </div>
                        <div className="registrationForm-Container-upper-container-second-text">
                            Please enter your email and password to login

                        </div>
                    </div>
                </div>
                <Form size='large' loading={this.state.loading} className='formContainer'>
                    <Header as='h2' style={{marginTop: '3%', fontFamily: 'Fahkwang'}} textAlign='center'>
                        Login
                    </Header>
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
                    <Form.Select
                        fluid
                        label='Type'
                        options={types}
                        placeholder='Type'
                        value={this.state.type}
                        error={this.state.errorType}
                        onChange={this.changeType}
                    />
                    <Button fluid size='large' style={{marginTop: '10%'}}onClick={this.login}>
                        Login
                    </Button>
                </Form>
            </div>)
        }
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(RegistrationForm));