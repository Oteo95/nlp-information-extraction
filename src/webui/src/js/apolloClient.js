import ApolloClient from 'apollo-boost'

export default new ApolloClient({
    uri: process.env.VUE_APP_GRAPHQL_API_ADDRS
})