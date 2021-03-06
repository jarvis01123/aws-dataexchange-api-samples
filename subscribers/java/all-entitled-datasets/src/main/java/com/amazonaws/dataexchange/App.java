package com.amazonaws.dataexchange;

import com.amazonaws.services.dataexchange.*;
import com.amazonaws.services.dataexchange.model.*;

public class App {
    public static void main(String[] args) {
        AWSDataExchange client = AWSDataExchangeClientBuilder.defaultClient();

        ListDataSetsRequest listDataSetsRequest = new ListDataSetsRequest()
                .withOrigin("ENTITLED");

        ListDataSetsResult dataSets = client.listDataSets(listDataSetsRequest);

        for (DataSetEntry dataSet : dataSets.getDataSets()) {
            System.out.printf("%s/%s: %s\n  %s\n",
                    dataSet.getOriginDetails().getProductId(),
                    dataSet.getId(),
                    dataSet.getName(),
                    dataSet.getDescription());
        }

        System.exit(0);
    }
}
