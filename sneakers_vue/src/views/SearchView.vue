<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>

                <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
            </div>

            <SneakersBox 
                v-for="sneakers in sneakers"
                v-bind:key="sneakers.id"
                v-bind:sneakers="sneakers" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import SneakersBox from '@/components/SneakersBox.vue'

export default {
    name: 'Search',
    components: {
        SneakersBox
    },
    data() {
        return {
            sneakers: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | Sneakers'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/v1/sneakers/search/', {'query': this.query})
                .then(response => {
                    this.sneakers = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
