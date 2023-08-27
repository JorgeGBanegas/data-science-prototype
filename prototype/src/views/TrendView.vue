<template>
    <div class="chart-page">
        <h1>
            Tendencia de precios de la vivienda
        </h1>
        <div v-if="series[0].data.length > 0" class="chart-container">
            <div class="chart">
                <apexchart type="line" height="350" width="800" :options="chartOptions" :series="series" />
            </div>
        </div>
        <button class="top-button" @click="goBack">Volver</button>
    </div>
</template>


<style>
.chart-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    background-color: #f2f2f2;
}

.back-button,
.top-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin: 10px;
}

.chart-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-grow: 1;
}

.chart {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
}
</style>

<script>
import chart from "vue-apexcharts";

export default {
    components: { apexchart: chart },
    data() {
        return {
            series: [{
                name: 'Promedio de Precios',
                type: 'column',
                data: []
            }, {
                name: 'Tendencia',
                type: 'line',
                data: []
            }],
            chartOptions: {
                chart: {
                    height: 350,
                    type: 'line',
                },
                stroke: {
                    width: [0, 4]
                },
                title: {
                    text: ''
                },
                dataLabels: {
                    enabled: true,
                    enabledOnSeries: [1]
                },
                labels: [2, 23,23],
                xaxis: {
                    type: 'float'
                },
                yaxis: [{
                    title: {
                        text: 'Promedio de precios',
                    },

                }]
            },
        }
    },
    async mounted() {
        await this.fetchTrendData();
    },
    methods: {
        goBack() {
            this.$router.push({ name: 'home' });
        },
        scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        },
        async fetchTrendData() {
            try {
                const response = await fetch(
                    'http://localhost:8000/analisis-tendencias',
                    {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    }
                );
                const data = await response.json();
                this.series[0].data = data.precios_promedio;
                this.series[1].data = data.tendencia;
                this.chartOptions.labels = data.anyos;

                //console.log("🚀 ~ file: TrendView.vue:71 ~ fetchTrendData ~ this.chartData:", this.chartData)
            } catch (error) {
                console.error('Error fetching trend data:', error);
            }
        }
    }
};
</script>