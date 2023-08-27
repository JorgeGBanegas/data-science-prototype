<template>
    <div class="container mt-5">
        <h2 class="mb-4">Realizar Valuación</h2>
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="bedroomAbvGr">Número de Dormitorios:</label>
                <input type="number" class="form-control" id="bedroomAbvGr" v-model="property.bedroomAbvGr" required>
            </div>
            <div class="form-group">
                <label for="fullBath">Baños Completos:</label>
                <input type="number" class="form-control" id="fullBath" v-model="property.fullBath" required>
            </div>
            <div class="form-group">
                <label for="lotArea">Área del Lote (metros cuadrados):</label>
                <input type="number" class="form-control" id="lotArea" v-model="property.lotArea" required>
            </div>
            <div class="form-group">
                <label for="grLivArea">Área Habitable (metros cuadrados):</label>
                <input type="number" class="form-control" id="grLivArea" v-model="property.grLivArea" required>
            </div>
            <button type="submit" class="btn btn-primary">Realizar Valuación</button>
        </form>
        <div v-if="valuationResult" class="mt-4">
            <h4>Resultado de la Valuación:</h4>
            <p>El precio estimado de la propiedad es: {{ valuationResult | currencyFormat }}</p>
        </div>
    </div>
</template>

<script>
export default {
    filters: {
        currencyFormat(value) {
            return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
        }
    },
    data() {
        return {
        property: {
            bedroomAbvGr: 0,
            fullBath: 0,
            lotArea: 0,
            grLivArea: 0
        },
        valuationResult: null
        };
    },
    methods: {
        async submitForm() {
            if (this.property.bedroomAbvGr <= 0 || this.property.fullBath <= 0 || this.property.lotArea <= 0 || this.property.grLivArea <= 0) {
                alert('Todos los campos son requeridos');
                return;
            }

            const lotAreaSqFt = this.property.lotArea * 10.7639; // 1 metro cuadrado = 10.7639 pies cuadrados
            const grLivAreaSqFt = this.property.grLivArea * 10.7639;
            const body = {
                "BedroomAbvGr": this.property.bedroomAbvGr,
                "FullBath": this.property.fullBath,
                "LotArea": lotAreaSqFt,
                "GrLivArea": grLivAreaSqFt
            }
            const response = await fetch('http://localhost:8000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(body)
            });
            const data = await response.json();
            console.log("🚀 ~ file: ValuationView.vue:66 ~ submitForm ~ data:", data)
            if (response.ok) {
                this.valuationResult = data.predicted_price;
                return;
            }
            console.error(data);
            alert('Error al realizar la valuación');
            return;

        }
    }
};
</script>

<style scoped>
.container {
    max-width: 600px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 20px;
}

.btn-primary {
    background-color: #007bff;
    border-color: #007bff;
}

.btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
}
</style>
