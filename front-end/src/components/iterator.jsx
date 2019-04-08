
export class DataIterator {


    function DataIterator (array) {
        this.array = array;
        this.size = array.length;
        this.index =0;
        this.hasNext = function(){
            return this.index<this.size;
        }
        this.next = function(){
            return this.array[this.index++];
        }
        this.reset = function(){
            this.index = 0;
        }
    }


}