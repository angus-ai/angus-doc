import java.awt.FlowLayout;
import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

import org.json.simple.JSONObject;

import ai.angus.sdk.Job;
import ai.angus.sdk.ProcessException;
import ai.angus.sdk.Root;
import ai.angus.sdk.Service;
import ai.angus.sdk.impl.ConfigurationImpl;
import ai.angus.sdk.impl.File;

import com.github.sarxos.webcam.Webcam;
import com.github.sarxos.webcam.WebcamResolution;

public class StreamAgeAndGender {

    public static void main(String[] args) throws IOException, ProcessException {
        ConfigurationImpl conf = new ConfigurationImpl();

        Root root = conf.connect();
        Service service = root.getServices().getService(
                "age_and_gender_estimation", 1);

        // get default webcam and open it
        Webcam webcam = Webcam.getDefault();
        webcam.setViewSize(WebcamResolution.QVGA.getSize());
        webcam.open();

        JFrame frame = new JFrame();
        frame.setLayout(new FlowLayout());
        frame.setSize(320, 240);
        JLabel lbl = new JLabel();
        frame.add(lbl);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        service.enableSession();
        while (true) {
            // get image
            BufferedImage image = webcam.getImage();

            ImageIO.write(image, "PNG", new java.io.File("/tmp/tmp.png"));
            JSONObject params = new JSONObject();
            params.put("image", new File("/tmp/tmp.png"));
            Job job = service.process(params);
            System.out.println(job.getResult().toJSONString());

            ImageIcon icon = new ImageIcon(image);
            lbl.setIcon(icon);
        }
    }
}
