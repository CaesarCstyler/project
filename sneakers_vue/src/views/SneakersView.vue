<template>
    <div class="page-sneakers">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="sneakers.get_image">
                </figure>

                <h1 class="title">{{ sneakers.name }}</h1>

                <p>{{ sneakers.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price: </strong>${{ sneakers.price }}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Sneakers',
    data() {
        return {
            sneakers: {},
            quantity: 1
        }
    },
    mounted() {
        this.getSneakers() 
    },
    methods: {
        async getSneakers() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const sneakers_slug = this.$route.params.sneakers_slug

            await axios
                .get(`/api/v1/sneakers/${category_slug}/${sneakers_slug}`)
                .then(response => {
                    this.sneakers = response.data

                    document.title = this.sneakers.name + ' | Sneakers'
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                sneakers: this.sneakers,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>
