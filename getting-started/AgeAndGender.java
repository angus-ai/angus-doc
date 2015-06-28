import java.io.IOException;
import org.json.simple.JSONObject;
import ai.angus.sdk.Configuration;
import ai.angus.sdk.Job;
import ai.angus.sdk.ProcessException;
import ai.angus.sdk.Root;
import ai.angus.sdk.Service;
import ai.angus.sdk.impl.ConfigurationImpl;
import ai.angus.sdk.impl.File;

public class AgeAndGender {

  public static void main(String[] args) throws IOException, ProcessException {
    Configuration conf = new ConfigurationImpl();

    Root root = conf.connect();
    Service service = root.getServices().getService("age_and_gender_estimation", 1);

    JSONObject params = new JSONObject();
    params.put("image", new File("./macgyver.jpg"));

    Job job = service.process(params);

    System.out.println(job.getResult().toJSONString());
 }
}
