import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Button, Loader, Tab} from 'semantic-ui-react'
import CartItem from './cartItem'
import DataIterator from "./iterator";
import axios from "axios";
import {Modal} from "antd";
import moment from "./availabilities";

var cartArray=[];
const confirm = Modal.confirm;

class Cart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            appointments: [],
            loading:false,
            availabilities: [],
            cartArray:[]
        }
    }

    componentDidMount() {
        cartArray=[];
        if(localStorage.getItem('cartAppointments')) {
        cartArray = JSON.parse(localStorage.getItem('cartAppointments'));
        var i =0
        cartArray.map(cartData=>{
            cartData.id=i;
            i=i+1;
        })
        this.setState({cartArray:cartArray})
        }
        this.getAvailabilities();
    }
    getAvailabilities=()=>{
        axios.get('http://127.0.0.1:5000/api/Availability').then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data.data)
                          let  array = response.data.data.sort(function compare(a, b) {
                                var dateA = moment(a.date || "YYYY-MM-DD HH:mm");
                                var dateB = moment(b.date || "YYYY-MM-DD HH:mm");
                                return dateA - dateB;
                            });
                        this.setState({availabilities: array})
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });
    }
    removeFromCart=(id)=>{
        let array =[];
        let Iterator =  new DataIterator(this.state.cartArray);
        var i = 0;
        while(Iterator.hasNext()){
            let cartItem = Iterator.next()
            if(cartItem.id !==id){
                array.push(cartItem)
            }
            i=i+1;

        }
        this.setState({cartArray:array})
        if(i !== 1) {
            localStorage.setItem('cartAppointments', JSON.stringify(array))
        }else{
            localStorage.removeItem("cartAppointments");
        }

    }
    removeAllCartItems=()=>{
       var this1= this;
         confirm({
    title: 'Are you sure to remove all cart items?',
    content: 'Note that this operation will remove permanently.',
    okText: 'Remove All',
    okType: 'danger',
    cancelText: 'Cancel',
    onOk() {
         localStorage.removeItem("cartAppointments");
        this1.setState({cartArray:[]})
        cartArray=[];
    },
  });
    }

    addAllAppointments=()=>{
        var this1 = this
        let Iterator =  new DataIterator(this.state.cartArray);
        while(Iterator.hasNext()){
            let data = Iterator.next()
            this.updateAvailability(data)
        }
        localStorage.removeItem("cartAppointments");
            this.setState({cartArray:[]})
            cartArray=[];
    }
    addAppointment=(data)=>{
        console.log(data)
        axios.post('http://127.0.0.1:5000/api/Appointment',data ).then(
                function (response, err) {
                    console.log(response)
                    if (response.data) {
                        console.log(response.data)
                    }
                }.bind(this)
            ).catch(error => {
                console.log(error)
            });

    }

    updateAvailability=(takenSpots)=>{
        var this1 = this
        var availabilityObject = false;
        this.state.availabilities.map(availabilityData=>{
            if(availabilityData.availability_id === takenSpots.availability_id){
                var i = 0;
                takenSpots.slots.map(takenSpotsSlots=>{
                    if(availabilityData.slots.includes(takenSpotsSlots)){
                        i=i+1;
                    }
                })
                if(takenSpots.slots.length === i) {
                        availabilityObject=availabilityData;
                }
            }
        })
        if(availabilityObject){
            takenSpots.slots.map(pointerData=> {
                if (availabilityObject.slots.includes(pointerData)) {
                    var index = availabilityObject.slots.indexOf(pointerData);
                    availabilityObject.slots.splice(index, 1);
                }
            })
            if(availabilityObject.slots.length === 0){
                    let data = availabilityObject;

                    axios.delete('http://127.0.0.1:5000/api/Availability',{data}).then(
                        function (response, err) {
                            console.log(response)
                            if (response.data) {
                                console.log(response.data.data)
                                this1.addAppointment(takenSpots)
                            }
                        }.bind(this)
                    ).catch(error => {
                        console.log(error)
                    });
                }else {

                    let data = availabilityObject
                    console.log(data)
                    axios.put('http://127.0.0.1:5000/api/Availability', data).then(
                        function (response, err) {
                            console.log(response)
                            if (response.data) {
                                console.log(response.data)
                                this1.addAppointment(takenSpots)
                            }
                        }.bind(this)
                    ).catch(error => {
                        console.log(error)
                    });
                }

        }else{
            localStorage.removeItem("cartAppointments");
            this.setState({cartArray:[]})
            cartArray=[];
        }

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
                             menuItem: "Appointments Cart",
                             render: () =>
                                 <Tab.Pane attached={false}>
                                    {this.state.cartArray.map(appointmentData => {
                                         return (<CartItem  appointments={appointmentData} removeFromCart={this.removeFromCart}/>);
                                     })}
                                 </Tab.Pane>
                         }
                     ]
                 }/>
                 {this.state.cartArray.length > 0 ?
                 <div className='footerTab'>
                     <Button  size={"small"} content='Remove All Cart Items' onClick={this.removeAllCartItems}/>
                     <Button size={"small"}  content='Pay & Book Appoinments' onClick={this.addAllAppointments}/>
                 </div> : null}
             </div>)
         }
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(Cart));