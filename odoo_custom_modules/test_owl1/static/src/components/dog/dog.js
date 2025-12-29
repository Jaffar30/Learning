/** @odoo-module **/

import { registry } from "@web/core/registry";
const { Component, useState,onWillStart ,useRef } = owl;
import {useService} from "@web/core/utils/hooks";

export class Dog extends Component {
    // constructor
    setup(){

        this.state = useState({
            dog:{name:"",color:"#4287f5",is_aggressive:false},
            dogs_list:[],
            isEdit:false,
            activeId:false
        });

        this.orm = useService("orm");
        this.model = "dog";
        this.searchInput = useRef("search_input");

        onWillStart(async()=>{
            await this.getAllDogs();
        })

    }

    // get all dogs
    async getAllDogs(){
        this.state.dogs_list = await this.orm.searchRead(this.model,[],['id','name','color','is_aggressive']);
    }

    // add new dog
    addDog(){}

    // edit dog
    editDog(dog){
        this.activeId = dog.id;
        this.state.isEdit = true;
        this.state.dog = {...dog};
    }

    async deleteDog(dog){
        await this.orm.unlink(this.model,[dog.id]);
        await this.getAllDogs();
    }

    // save dog
    async saveDog(){
        
        if(this.state.isEdit){
            await this.orm.write(this.model,[this.activeId],{
                name:this.state.dog.name,
                color:this.state.dog.color,
                is_aggressive:this.state.dog.is_aggressive
            });

        }else{

            await this.orm.create(this.model,[
                {
                    name:this.state.dog.name,
                    color:this.state.dog.color,
                    is_aggressive:this.state.dog.is_aggressive
                }
            ]);

        }

        this.resetValues();
        await this.getAllDogs();
    }

    // reset values
    resetValues(){
        this.state.dog = {name:"",color:"#4287f5",is_aggressive:false};
        this.state.isEdit = false;
        this.activeId = false;
    }

    // search function
    async searchDog(){
        const input = this.searchInput.el.value;
        this.state.dogs_list = await this.orm.searchRead(this.model,[['name','ilike',input]],['id','name','color','is_aggressive']);
        // this.state.dogs_list = await user_dog;
    }

    // check and uncheck aggressive
    async toggleAggressive(e,dog){
        await this.orm.write(this.model,[dog.id],{
            is_aggressive:e.target.checked
        });

        await this.getAllDogs();
    }

    // change color
    async changeColor(e,dog){
        await this.orm.write(this.model,[dog.id],{
            color:e.target.value
        });
    }

    // 🦎 Make the browser speak "Lizard"
    sayLizard() {
        const msg = new SpeechSynthesisUtterance("Lizard!");
        msg.lang = "en-US"; // You can change to "en-GB" or "en-AU" etc.
        msg.rate = 0.8;     // Slightly faster = more meme energy
        msg.pitch = 8.4;    // Higher pitch = funnier tone
        speechSynthesis.cancel(); // stop any previous voice
        speechSynthesis.speak(msg);
    }
    
}
// add class template(view)
Dog.template = "test_owl1.DogTemplate";
// add class action to registry
registry.category("actions").add("dog_js_action",Dog);
