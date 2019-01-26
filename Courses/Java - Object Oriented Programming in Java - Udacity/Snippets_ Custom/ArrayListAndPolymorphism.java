// 2018.05.31

// Whole point of using polymorphism with polymorphism is
// to allow to retrieve items as if they were the parent type
// and then simply use common method that would exist in any of its children.

// package _MySnippets.polymorphism;

import java.util.ArrayList;

public class ArrayListAndPolymorphism {

    public static void main(String[] args) {
        ArrayList<Media> playlist = new ArrayList<>();

        //------------------------------------------------------
        System.out.println("\n---Audio Start---\n");

        playlist.add(new Audio());

        Media mediaAudio = playlist.get(0);
        Audio audio = (Audio) playlist.get(0);
        Audio audioCastedSoMuch =
                (Audio)
                        (Media)
                                (Audio)
                                        (Media)
                                                (Audio) playlist.get(0);

        mediaAudio.play();
        System.out.println(mediaAudio.title + " made by " + mediaAudio.company
                + " ( Volume: " + mediaAudio.volume + " ) ( Format: " + "System.out.println(mediaAudio.audioFormat); Causes Error" + " )");

        audio.play();
        System.out.println(audio.title + " made by " + audio.company
                + " ( Volume: " + audio.volume + " ) ( Format: " + audio.audioFormat + " )");

        audioCastedSoMuch.play();
        System.out.println(audioCastedSoMuch.title + " made by " + audioCastedSoMuch.company
                + " ( Volume: " + audioCastedSoMuch.volume + " ) ( Format: " + audioCastedSoMuch.audioFormat + " )");

        /*
        Because Media doesn't have an audioFormat variable, below statement causes the following Error.
          System.out.println(mediaAudio.audioFormat);
            Error: (32, 92)
            java: cannot find symbol
            symbol: variable audioFormat
            location: variable mediaAudio of type Media
        */

        //------------------------------------------------------
        System.out.println("\n---Video Start---\n");


        playlist.add(new VideoYes_This());
        playlist.add(new VideoYes_Super());

        playlist.add(new VideoNo_NewVar());
        playlist.add(new VideoNo_This());

        playlist.add(new VideoMaybe_Super());


        Media mediaVideoYes_This = playlist.get(1);
        VideoYes_This videoYes_This = (VideoYes_This) playlist.get(1);

        Media mediaVideoYes_Super = playlist.get(2);
        VideoYes_Super videoYes_Super = (VideoYes_Super) playlist.get(2);


        Media mediaVideoNo_NewVar = playlist.get(3);
        VideoNo_NewVar videoNo_NewVar = (VideoNo_NewVar) playlist.get(3);

        Media mediaVideoNo_This = playlist.get(4);
        VideoNo_This videoNo_This = (VideoNo_This) playlist.get(4);


        Media mediaVideoMaybe_Super = playlist.get(5);
        VideoMaybe_Super videoMaybe_Super = (VideoMaybe_Super) playlist.get(5);


        System.out.println();

        mediaVideoYes_This.play();
        System.out.println(mediaVideoYes_This.title + " made by " + mediaVideoYes_This.company
                + " ( Volume: " + mediaVideoYes_This.volume + " ) ( Format: " + mediaVideoYes_This.videoFormat + " )");
        videoYes_This.play();
        System.out.println(videoYes_This.title + " made by " + videoYes_This.company
                + " ( Volume: " + videoYes_This.volume + " ) ( Format: " + videoYes_This.videoFormat + " )");


        mediaVideoYes_Super.play();
        System.out.println(mediaVideoYes_Super.title + " made by " + mediaVideoYes_Super.company
                + " ( Volume: " + mediaVideoYes_Super.volume + " ) ( Format: " + mediaVideoYes_Super.videoFormat + " )");
        videoYes_Super.play();
        System.out.println(videoYes_Super.title + " made by " + videoYes_Super.company
                + " ( Volume: " + videoYes_Super.volume + " ) ( Format: " + videoYes_Super.videoFormat + " )");

        System.out.println();


        mediaVideoNo_NewVar.play();
        System.out.println(mediaVideoNo_NewVar.title + " made by " + mediaVideoNo_NewVar.company
                + " ( Volume: " + mediaVideoNo_NewVar.volume + " ) ( Format: " + mediaVideoNo_NewVar.videoFormat + " )");
        videoNo_NewVar.play();
        System.out.println(videoNo_NewVar.title + " made by " + videoNo_NewVar.company
                + " ( Volume: " + videoNo_NewVar.volume + " ) ( Format: " + videoNo_NewVar.videoFormat + " )");


        mediaVideoNo_This.play();
        System.out.println(mediaVideoNo_This.title + " made by " + mediaVideoNo_This.company
                + " ( Volume: " + mediaVideoNo_This.volume + " ) ( Format: " + mediaVideoNo_This.videoFormat + " )");
        videoNo_This.play();
        System.out.println(videoNo_This.title + " made by " + videoNo_This.company
                + " ( Volume: " + videoNo_This.volume + " ) ( Format: " + videoNo_This.videoFormat + " )");

        System.out.println();


        mediaVideoMaybe_Super.play();
        System.out.println(mediaVideoMaybe_Super.title + " made by " + mediaVideoMaybe_Super.company
                + " ( Volume: " + mediaVideoMaybe_Super.volume + " ) ( Format: " + mediaVideoMaybe_Super.videoFormat + " )");
        videoMaybe_Super.play();
        System.out.println(videoMaybe_Super.title + " made by " + videoMaybe_Super.company
                + " ( Volume: " + videoMaybe_Super.volume + " ) ( Format: " + videoMaybe_Super.videoFormat + " )");






/*
      Because Media has the videoFormat variable,
        System.out.println(mediaVideoYes_This.videoFormat);
      doesn't causes an Error.
*/

    }
}

class Entertainment {
    String company = "Hyeogikarp";
}

class Media extends Entertainment {
    String title = "! Media";
    int volume = 0;
    //String audioFormat = "MediaAudio!"
    String videoFormat = "! Media's Format";

    void play() {
        System.out.println("! Playing \"Media\"");
    }
}

class Audio extends Media {
    String audioFormat = "Audio's Format";

    Audio() {
        this.title = "Audio";
        this.volume = 100;
    }

    @Override
    void play() {
        System.out.println("Playing Audio");
    }
}

class VideoYes_This extends Media {
    VideoYes_This() {
        this.title = "VideoYes_This";
        this.volume = 150;
        this.videoFormat = "This's Format";
    }

    @Override
    void play() {
        System.out.println("Playing VideoYes_This");
    }
}

class VideoYes_Super extends Media {
    VideoYes_Super() {
        super.title = "VideoYes_Super";
        super.volume = 150000;
        super.videoFormat = "Super's Format";
    }

    @Override
    void play() {
        System.out.println("Playing VideoYes_Super");
    }
}

class VideoNo_NewVar extends Media {
    String title = "VideoNo_NewVar's newVar";
    int volume = 98;
    String videoFormat = "newVar's Format";

    VideoNo_NewVar() {
    }

    @Override
    void play() {
        System.out.println("Playing VideoNo_NewVar");
    }
}

class VideoNo_This extends Media {
    String title = "VideoNo_This's newVar";
    int volume = 980;
    String videoFormat = "newVar's Format";

    VideoNo_This() {
        this.title = "VideoNo_This";
        this.volume = 300;
        this.videoFormat = "This's Format";
    }

    @Override
    void play() {
        System.out.println("Playing VideoNo_This");
    }
}

class VideoMaybe_Super extends Media {
    String title = "VideoMaybe_Super's newVar";
    int volume = 9800;
    String videoFormat = "newVar's Format";

    VideoMaybe_Super() {
        super.title = "VideoMaybe_Super";
        super.volume = 300;
        super.videoFormat = "Super's Format";
    }

    @Override
    void play() {
        System.out.println("Playing VideoMaybe_Super");
    }
}