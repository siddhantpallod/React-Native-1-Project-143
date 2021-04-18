import React, { Component } from 'react'
import { Text, View, TouchableOpacity } from 'react-native'
import { Header, Icon } from 'react-native-elements';
import WebView from 'react-native-webview';
import axios from 'axios';

export default class Home extends Component {

    constructor(){
        super();
        this.state = {
            articleDetails:{}
        }
    }

    componentDidMount(){
        this.getArticle()
    }

    getArticle = () => {
        const url = "http://localhost:5000/get-article"
        axios.get(url).then(response => {
            this.setState({articleDetails: response.data.data})
        }).catch((error) =>{
            alert(error.message)
        })
    }

    likedArticle = () => {
        const url = "http://localhost:5000/liked-articles";
        axios.post(url).then(response => {
            this.getArticle()
        }).catch((error) => {
            alert(error.message)
        })
    }

    unlikedArticle = () => {
        const url = "http://localhost:5000/unliked-articles";
        axios.post(url).then(response => {
            this.getArticle()
        })
        .catch((error) => {
            alert(error.message)
        })
    }

    render() {
        const {articleDetails} = this.state;
        if(articleDetails.url){
            const {url} = articleDetails
        
        return (
            <View>
                <View>
                    <Header 
                        centerComponent = {{
                            text: 'Articles'
                        }}
                        backgroundColor = {"#d500f9"}
                        containerStyle = {{flex: 1}}
                    />
                </View>
                <View>
                    <WebView source = {{uri: url}} />
                </View>
                <View>
                    <TouchableOpacity onPress = {this.likedArticle}>
                        <Icon reverse name = {'check'} type = {'entypo'} color = {"#76ff03"} />
                    </TouchableOpacity>
                    <TouchableOpacity onPress = {this.unlikedArticle}>
                        <Icon reverse name = {'cross'} type = {'entypo'} color = {'#ff1744'} />
                    </TouchableOpacity>
                </View>
            </View>
        )
    }
    return null;
    }
}
