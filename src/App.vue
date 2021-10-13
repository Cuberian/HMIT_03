<template>
  <div id="app" class="flex-container">
    <div class="">
      <h2>FORM FOR LAB 3</h2>
      <form action="" @submit.prevent="sendFilter" ref="formItem">
        <p class="flex-row"><span>AGE:</span> <input type="number" value="56" name="age"></p>
        <p class="flex-row"><span>WORKCLASS:</span> <input type="text" value="Local-gov" name="workclass"></p>
        <p class="flex-row"><span>FNLWGT:</span> <input type="number" value="216851" name="fnlwgt"></p>
        <p class="flex-row"><span>EDUCATION:</span> <input type="text" value="Bachelors" name="education"></p>
        <p class="flex-row"><span>EDUCATION-NUM:</span> <input type="number" value="13" name="education-num"></p>
        <p class="flex-row"><span>MARITAL-STATUS:</span> <input type="text" value="Married-civ-spouse" name="marital-status"></p>
        <p class="flex-row"><span>OCCUPATION:</span> <input type="text" value="Tech-support" name="occupation" ></p>
        <p class="flex-row"><span>RELATIONSHIP:</span> <input type="text" value="Husband" name="relationship"></p>
        <p class="flex-row"><span>RACE:</span> <input type="text" value="White" name="race"></p>
        <p class="flex-row"><span>SEX:</span> <input type="text" value="Male" name="sex"></p>
        <p class="flex-row"><span>CAPITAL-GAIN:</span> <input type="number" value="0" name="capital-gain"></p>
        <p class="flex-row"><span>CAPITAL-LOSS:</span> <input type="number" value="0" name="capital-loss"></p>
        <p class="flex-row"><span>HOUR-PER-WEEK:</span> <input type="number" value="40" name="hours-per-week"></p>
        <p class="flex-row"><span>NATIVE-COUNTRY:</span> <input type="text" value="United-States" name="native-country"></p>
        <p class="flex-row">INCOME: <input type="text" name="income"></p>
        <button type="submit">FIND</button>
      </form>
    </div>
    <div>
      <h2>Results</h2>
      <div v-if="result">
        <p>Scored Labels: {{ result[0] }}</p>
        <p>Scored Probabilities: {{ result[1] }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data () {
    return {
      columnsArray: [
        "age",
        "workclass",
        "fnlwgt",
        "education",
        "education-num",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital-gain",
        "capital-loss",
        "hours-per-week",
        "native-country",
        "income"
      ],
      result: null
    }
  },
  methods: {
    async sendFilter () {
      const formData = new FormData(this.$refs.formItem)
      console.log(formData.values)
      const { data } = await axios.post('http://127.0.0.1:5000/find',
          {
        "Inputs": {
        "input1": {
          "ColumnNames": this.columnsArray,
          "Values": [this.columnsArray.map( column => formData.get(column))]
        } }, "GlobalParameters": {} }, { headers: {"Access-Control-Allow-Origin": "*"}})
      this.result = data.Results.output1.value.Values[0].slice(-2)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.flex-container {
  display: flex;
  justify-content: space-around;
}
.flex-row {
  display: flex;
  justify-content: space-between;
}
</style>
