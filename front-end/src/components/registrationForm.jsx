import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Select, Form, Header} from 'semantic-ui-react'
import DoctorRegistration from './doctorRegistration';
import PatirentRegistration from './patientRegistration';
import NurseRegistration from './nurseRegistration';

const types = [
    {key: 'Doctor', value: 'Doctor', text: 'Doctor'},
    {key: 'Patient', value: 'Patient', text: 'Patient'},
    {key: 'Nurse', value: 'Nurse', text: 'Nurse'}
]
class RegistrationForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            type:'',
            loading:false,
        }
    }

    componentDidMount() {

    }
    changeType=(e, {value})=>{
        this.setState({type: value})
        this.setState({errorType: false})
    }

    render() {
        return (<div className='registrationForm-Container'>
            <div className="registrationForm-Container-upper-container">
                <div className="registrationForm-Container-upper-container-text">
                    <div className="registrationForm-Container-upper-container-first-text">
                        Registration
                    </div>
                    <div className="registrationForm-Container-upper-container-second-text">
                        {this.state.type? 'Please enter your personal information' :'Please choose account type to register'}

                    </div>
                </div>
                {this.state.type?
                <Select
                    style={{width:'20%'}}
                    fluid
                    label='Change Type'
                    options={types}
                    value={this.state.type}
                    error={this.state.errorType}
                    onChange={this.changeType}
                />: ''}
            </div>
            {this.state.type?
                (this.state.type === 'Doctor'?
                    <DoctorRegistration/>:
                    this.state.type === 'Patient'?
                        <PatirentRegistration/>: <NurseRegistration/>)
                :
            <Form size='large'  loading={this.state.loading} className='formContainer'>
                <Header as='h2'  style={{marginTop:'3%', fontFamily: 'Fahkwang'}}textAlign='center'>
                    Choose Account Type
                </Header>
                <Form.Select
                    fluid
                    label='Type'
                    placeholder='Ex: Patient'
                    options={types}
                    value={this.state.type}
                    error={this.state.errorType}
                    onChange={this.changeType}
                />
            </Form>}
        </div>)
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(RegistrationForm));