import java.awt.FlowLayout;
import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

import com.github.sarxos.webcam.Webcam;
import com.github.sarxos.webcam.WebcamResolution;

public class DisplayCamera {

    public static void main(String[] args) throws IOException {

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

        while (true) {
            // get image
            BufferedImage image = webcam.getImage();

            ImageIcon icon = new ImageIcon(image);
            lbl.setIcon(icon);
        }

    }
}
