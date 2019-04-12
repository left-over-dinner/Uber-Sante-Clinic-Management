
export default class DataIterator {
    constructor(array){
        this.array = array;
        this.size = array.length;
        this.index =0;
    }
    hasNext(){
        return this.index<this.size;
    }
    next(){
        return this.array[this.index++];
    }
    reset() {
        this.index=0;
    }
    //DataIterator =()=>{}


}